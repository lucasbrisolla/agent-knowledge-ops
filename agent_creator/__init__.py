"""Fábrica local de scaffolds de Agent Products."""

from .core import ProductSpec, create_from_spec, create_product, load_spec, validate_product

__all__ = [
    "ProductSpec",
    "create_from_spec",
    "create_product",
    "load_spec",
    "validate_product",
]
