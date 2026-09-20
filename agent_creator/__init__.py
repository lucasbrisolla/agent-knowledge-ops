"""Fábrica local de scaffolds de Agent Products."""

from .core import (
    DEFAULT_TARGET_USER,
    PRODUCT_STATUSES,
    RECOMMENDED_FORMS,
    STATE_VALUES,
    VERIFICATION_VALUES,
    ProductSpec,
    create_from_spec,
    create_product,
    load_spec,
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
    "validate_product",
]
