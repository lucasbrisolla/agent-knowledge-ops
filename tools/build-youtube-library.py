#!/usr/bin/env python3
"""Gera uma biblioteca Markdown de YouTube a partir de arquivos do yt-dlp."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


VIDEO_URL = "https://www.youtube.com/watch?v={video_id}"


DEFAULT_CATEGORY_RULES: list[tuple[str, list[str]]] = [
    ("Resumo & Cover Letter", ["resume", "cover letter", "ats", "applicant tracking", "cv"]),
    ("Entrevistas", ["interview", "interviewer", "tell me about yourself", "why should we hire you"]),
    ("Salário & Negociação", ["salary", "negotiation", "negotiate", "paid", "paycheck", "counter offer"]),
    ("Demissões & Desemprego", ["layoff", "laid off", "unemployment", "job loss", "fired", "recession"]),
    ("LinkedIn & Marca Pessoal", ["linkedin", "personal brand", "profile"]),
    ("Busca De Emprego", ["job search", "job seeker", "job application", "rejected", "ghost", "get a job"]),
    ("Carreira & Crescimento", ["career change", "career advice", "career path", "promotion", "skills", "mba"]),
    ("Trabalho & Gestão", ["boss", "manager", "toxic", "workplace", "coworker", "burnout", "company"]),
    ("Recrutamento & RH", ["recruiter", "recruiting", "hiring manager", "hr", "background check"]),
    ("Mercado & Trabalho Remoto", ["remote", "job market", "labor market", "great resignation"]),
    ("Empreendedorismo & Renda Paralela", ["side hustle", "side income", "entrepreneur", "freelance"]),
    ("Atualizações Do Canal", ["channel update", "life update", "my backstory", "live stream"]),
]


@dataclass
class VideoNote:
    title: str
    category: str
    video_id: str
    channel: str
    upload_date: str
    duration: str
    url: str
    status: str
    note_path: Path
    subtitle_path: Path | None
    metadata_path: Path
    playlist_index: int | None


def main() -> int:
    parser = argparse.ArgumentParser(description="Cria videos/*.md e index.md a partir de raw/*.info.json.")
    parser.add_argument("--raw-dir", default="raw", help="Diretório com .info.json e .srt")
    parser.add_argument("--videos-dir", default="videos", help="Diretório para notas por vídeo")
    parser.add_argument("--index", default="index.md", help="Caminho do índice Markdown")
    parser.add_argument("--readme", default="README.md", help="Caminho do README do projeto")
    parser.add_argument("--channel-name", default="", help="Nome do canal para o título do índice")
    parser.add_argument("--categories", default="", help="JSON opcional com {categoria: [palavras-chave]}")
    parser.add_argument("--overwrite", action="store_true", help="Sobrescreve notas Markdown existentes")
    args = parser.parse_args()

    root = Path.cwd()
    raw_dir = root / args.raw_dir
    videos_dir = root / args.videos_dir
    index_path = root / args.index
    readme_path = root / args.readme

    if not raw_dir.exists():
        raise SystemExit(f"Diretório raw não encontrado: {raw_dir}")

    category_rules = load_category_rules(args.categories)
    videos_dir.mkdir(parents=True, exist_ok=True)

    notes: list[VideoNote] = []
    for metadata_path in sorted(raw_dir.glob("*.info.json")):
        metadata = load_metadata(metadata_path)
        if metadata.get("_type") not in (None, "video"):
            continue

        note = build_note(metadata, metadata_path, raw_dir, videos_dir, category_rules)
        write_video_note(note, metadata, args.overwrite)
        notes.append(note)

    notes.sort(key=sort_key)
    channel_name = args.channel_name or infer_channel_name(notes) or "Biblioteca Do Canal"
    write_index(index_path, notes, channel_name)
    write_readme(readme_path, notes, channel_name, raw_dir, videos_dir)

    with_transcript = sum(1 for note in notes if note.subtitle_path)
    print(f"Índice gerado: {index_path}")
    print(f"README gerado: {readme_path}")
    print(f"Notas de vídeo: {len(notes)}")
    print(f"Com transcrição: {with_transcript}")
    print(f"Sem transcrição: {len(notes) - with_transcript}")
    return 0


def load_category_rules(path: str) -> list[tuple[str, list[str]]]:
    if not path:
        return DEFAULT_CATEGORY_RULES

    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [(str(category), [str(keyword) for keyword in keywords]) for category, keywords in data.items()]


def load_metadata(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"JSON inválido em {path}: {exc}") from exc


def build_note(
    metadata: dict,
    metadata_path: Path,
    raw_dir: Path,
    videos_dir: Path,
    category_rules: list[tuple[str, list[str]]],
) -> VideoNote:
    video_id = required(metadata, "id", metadata_path)
    title = metadata.get("title") or metadata.get("fulltitle") or video_id
    category = categorize_title(title, category_rules)
    upload_date = format_upload_date(metadata.get("upload_date"))
    duration = format_duration(metadata.get("duration")) or metadata.get("duration_string") or ""
    channel = metadata.get("channel") or metadata.get("uploader") or ""
    url = metadata.get("webpage_url") or VIDEO_URL.format(video_id=video_id)
    playlist_index = metadata.get("playlist_index")
    subtitle_path = find_subtitle(raw_dir, video_id)
    status = "transcribed" if subtitle_path else "missing_transcript"
    filename = make_note_filename(upload_date, video_id, title)

    return VideoNote(
        title=str(title),
        category=category,
        video_id=video_id,
        channel=str(channel),
        upload_date=upload_date,
        duration=duration,
        url=str(url),
        status=status,
        note_path=videos_dir / category / filename,
        subtitle_path=subtitle_path,
        metadata_path=metadata_path,
        playlist_index=playlist_index if isinstance(playlist_index, int) else None,
    )


def categorize_title(title: str, category_rules: list[tuple[str, list[str]]]) -> str:
    normalized = normalize_for_matching(title)
    for category, keywords in category_rules:
        if any(normalize_for_matching(keyword).strip() in normalized for keyword in keywords):
            return category
    return "Geral"


def required(metadata: dict, key: str, path: Path) -> str:
    value = metadata.get(key)
    if not value:
        raise SystemExit(f"Campo obrigatório {key!r} ausente em {path}")
    return str(value)


def find_subtitle(raw_dir: Path, video_id: str) -> Path | None:
    candidates = list(raw_dir.glob(f"*{video_id}*.srt"))
    if not candidates:
        return None

    def rank(path: Path) -> tuple[int, str]:
        name = path.name
        if ".pt-orig.srt" in name or ".en-orig.srt" in name:
            return (0, name)
        if ".pt.srt" in name or ".en.srt" in name:
            return (1, name)
        return (2, name)

    return sorted(candidates, key=rank)[0]


def write_video_note(note: VideoNote, metadata: dict, overwrite: bool) -> None:
    if note.note_path.exists() and not overwrite:
        return

    note.note_path.parent.mkdir(parents=True, exist_ok=True)
    transcript = parse_srt(note.subtitle_path) if note.subtitle_path else []
    description = clean_description(metadata.get("description") or "")
    chapters = metadata.get("chapters") or []
    tags = metadata.get("tags") or []

    body = [
        "---",
        f"title: {yaml_string(note.title)}",
        f"youtube_id: {yaml_string(note.video_id)}",
        f"channel: {yaml_string(note.channel)}",
        f"url: {yaml_string(note.url)}",
        f"published: {yaml_string(note.upload_date)}",
        f"duration: {yaml_string(note.duration)}",
        f"category: {yaml_string(note.category)}",
        f"status: {yaml_string(note.status)}",
        'source: "youtube"',
        f"raw_metadata: {yaml_string(str(note.metadata_path))}",
    ]
    if note.subtitle_path:
        body.append(f"raw_transcript: {yaml_string(str(note.subtitle_path))}")
    if tags:
        body.append("tags:")
        for tag in tags[:20]:
            body.append(f"  - {yaml_string(str(tag))}")
    body.extend(["---", "", f"# {note.title}", "", "## Metadados", ""])
    body.extend(
        [
            f"- Canal: {note.channel}",
            f"- Publicado em: {note.upload_date}",
            f"- Duração: {note.duration}",
            f"- Categoria: {note.category}",
            f"- URL: {note.url}",
            f"- Status: {note.status}",
            "",
        ]
    )

    if chapters:
        body.extend(["## Capítulos", ""])
        for chapter in chapters:
            start = format_duration(chapter.get("start_time"))
            title = chapter.get("title") or "Sem título"
            body.append(f"- [{start}] {title}")
        body.append("")

    if description:
        body.extend(["## Descrição", "", description, ""])

    body.extend(["## Transcrição", ""])
    if transcript:
        for timestamp, text in transcript:
            body.extend([f"[{timestamp}] {text}", ""])
    else:
        body.extend(["_Transcrição não disponível nos arquivos extraídos._", ""])

    note.note_path.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")


def parse_srt(path: Path | None) -> list[tuple[str, str]]:
    if not path:
        return []

    text = path.read_text(encoding="utf-8", errors="replace")
    blocks = re.split(r"\n\s*\n", text.replace("\r\n", "\n").replace("\r", "\n"))
    transcript: list[tuple[str, str]] = []
    last_line = ""

    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        time_line_index = next((i for i, line in enumerate(lines) if "-->" in line), None)
        if time_line_index is None:
            continue

        timestamp = lines[time_line_index].split("-->", 1)[0].strip().split(",", 1)[0]
        for caption_line in lines[time_line_index + 1 :]:
            caption_line = normalize_caption(caption_line)
            if caption_line and caption_line != last_line:
                transcript.append((timestamp, caption_line))
                last_line = caption_line

    return transcript


def write_index(path: Path, notes: list[VideoNote], channel_name: str) -> None:
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    with_transcript = sum(1 for note in notes if note.subtitle_path)
    body = [
        f"# {channel_name}",
        "",
        f"Gerado em: {generated_at}",
        "",
        "## Resumo",
        "",
        f"- Vídeos indexados: {len(notes)}",
        f"- Com transcrição: {with_transcript}",
        f"- Sem transcrição: {len(notes) - with_transcript}",
        "",
        "## Categorias",
        "",
        "| Categoria | Vídeos |",
        "|---|---:|",
    ]

    for category, count in category_counts(notes):
        body.append(f"| {escape_table(category)} | {count} |")

    body.extend(["", "## Vídeos", "", "| Publicado | Categoria | Vídeo | Duração | Status |", "|---|---|---|---:|---|"])
    for note in notes:
        link = note.note_path.relative_to(path.parent).with_suffix("")
        body.append(
            f"| {note.upload_date} | {escape_table(note.category)} | "
            f"[[{link}|{escape_table(note.title)}]] | {note.duration} | {note.status} |"
        )

    body.extend(["", "## Por Categoria", ""])
    for category in sorted({note.category for note in notes}):
        body.extend([f"### {category}", ""])
        for note in notes:
            if note.category == category:
                link = note.note_path.relative_to(path.parent).with_suffix("")
                body.append(f"- [[{link}|{note.upload_date} - {note.title}]]")
        body.append("")

    path.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")


def write_readme(path: Path, notes: list[VideoNote], channel_name: str, raw_dir: Path, videos_dir: Path) -> None:
    with_transcript = sum(1 for note in notes if note.subtitle_path)
    body = [
        f"# {channel_name} — Biblioteca De Transcrições",
        "",
        "Biblioteca local gerada a partir de arquivos do `yt-dlp`.",
        "",
        "## Estrutura",
        "",
        f"- `{raw_dir.name}/`: metadados e transcrições brutas.",
        f"- `{videos_dir.name}/`: notas Markdown por vídeo.",
        "- `index.md`: catálogo principal.",
        "",
        "## Estado Atual",
        "",
        f"- Vídeos indexados: {len(notes)}",
        f"- Com transcrição: {with_transcript}",
        f"- Sem transcrição: {len(notes) - with_transcript}",
        "",
        "## Próximo Passo Editorial",
        "",
        "Escolher os vídeos de maior valor e aplicar `youtube-distillation` antes de promover qualquer conhecimento para o agente.",
    ]
    path.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")


def infer_channel_name(notes: list[VideoNote]) -> str:
    for note in notes:
        if note.channel:
            return note.channel
    return ""


def category_counts(notes: list[VideoNote]) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for note in notes:
        counts[note.category] = counts.get(note.category, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


def sort_key(note: VideoNote) -> tuple[str, int]:
    playlist_index = note.playlist_index if note.playlist_index is not None else 999999
    return (note.upload_date or "0000-00-00", playlist_index)


def make_note_filename(upload_date: str, video_id: str, title: str) -> str:
    date = upload_date if upload_date else "unknown-date"
    return f"{date}-{video_id}-{slugify(title)}.md"


def slugify(value: str, max_length: int = 90) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-z0-9]+", "-", value.lower())
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return (value[:max_length].rstrip("-") or "untitled")


def normalize_for_matching(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-z0-9+#]+", " ", text.lower())
    return f" {re.sub(r'\s+', ' ', text).strip()} "


def normalize_caption(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r"\s+", " ", text).strip()


def format_upload_date(value: str | None) -> str:
    if not value or len(value) != 8:
        return ""
    return f"{value[:4]}-{value[4:6]}-{value[6:8]}"


def format_duration(value: object) -> str:
    if value in (None, ""):
        return ""
    try:
        total = int(float(value))
    except (TypeError, ValueError):
        return str(value)

    hours, remainder = divmod(total, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def clean_description(description: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", description.strip())


def yaml_string(value: str) -> str:
    return json.dumps(value or "", ensure_ascii=False)


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


if __name__ == "__main__":
    raise SystemExit(main())
