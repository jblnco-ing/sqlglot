"""
Simplify redundant LIKE predicates.
"""

from __future__ import annotations

import typing as t

from sqlglot import exp


class LikeSimplifier:
    """Responsible for reducing redundant LIKE predicates."""

    def simplify(self, likes: list) -> list:
        """Simplify a list of LIKE predicates."""
        return likes
