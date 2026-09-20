from __future__ import annotations

import json
import subprocess
from pathlib import Path

from source_project import validate_project


ROOT = Path(__file__).resolve().parents[1]
CREATE = ROOT / "tools" / "create-source-project.py"
BUILD = ROOT / "tools" / "build-youtube-library.py"


def test_builds_youtube_library_inside_a_source_project(tmp_path: Path) -> None:
    project = tmp_path / "career-channel"
    created = subprocess.run(
        [
            "python3",
            str(CREATE),
            str(project),
            "--template",
            "youtube",
            "--source-name",
            "Career Channel",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert created.returncode == 0, created.stderr

    (project / "raw" / "video-1.info.json").write_text(
        json.dumps(
            {
                "_type": "video",
                "id": "video-1",
                "title": "Salary negotiation basics",
                "channel": "Career Channel",
                "upload_date": "20260920",
                "duration": 125,
                "webpage_url": "https://youtube.com/watch?v=video-1",
                "description": "A practical guide.",
                "chapters": [{"start_time": 0, "title": "Opening"}],
                "tags": ["salary"],
            }
        ),
        encoding="utf-8",
    )
    (project / "raw" / "video-1.en-orig.srt").write_text(
        "1\n00:00:00,000 --> 00:00:02,000\nNegotiate with evidence.\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        ["python3", str(BUILD), "--project", str(project)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stderr
    note = next((project / "library" / "videos").rglob("*.md"))
    assert "Negotiate with evidence." in note.read_text(encoding="utf-8")
    assert (project / "library" / "index.md").is_file()
    assert (project / "library" / "README.md").is_file()
    assert not (project / "videos").exists()
    assert validate_project(project).errors == ()
