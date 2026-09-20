"""Adapter de compatibilidade para o core interno ``agent_creator``."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agent_creator.core import (  # noqa: E402
    DEFAULT_TARGET_USER,
    PRODUCT_STATUSES,
    RECOMMENDED_FORMS,
    STATE_VALUES,
    VERIFICATION_VALUES,
    ProductSpec,
    create_from_spec,
    create_product,
    load_spec,
    slugify,
    validate_product,
)

__all__ = [
    "ProductSpec",
    "DEFAULT_TARGET_USER",
    "PRODUCT_STATUSES",
    "RECOMMENDED_FORMS",
    "STATE_VALUES",
    "VERIFICATION_VALUES",
    "create_from_spec",
    "create_product",
    "load_spec",
    "slugify",
    "validate_product",
]
