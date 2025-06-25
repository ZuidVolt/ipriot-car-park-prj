from typing import TypeGuard

type Uint = int


def strip_dunder(s: str) -> str:
    """Remove leading and trailing double underscores from a string."""
    return s.strip("_")


def is_uint(integer: int | Uint) -> TypeGuard[Uint]:
    """Check if the given integer is a non-negative integer"""
    return isinstance(integer, int | Uint) and integer > 0
