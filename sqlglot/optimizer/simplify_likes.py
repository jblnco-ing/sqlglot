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
        if len(likes) <= 1:
            return likes

        # Remove duplicates while preserving order
        seen = set()
        unique_likes = []
        for item in likes:
            if item not in seen:
                seen.add(item)
                unique_likes.append(item)

        # Remove elements that have a prefix in the list
        result = []
        for item in unique_likes:
            has_prefix = False
            for other in unique_likes:
                if item != other and item.startswith(other):
                    has_prefix = True
                    break
            if not has_prefix:
                result.append(item)

        return result
