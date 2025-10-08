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
            return [item.lower() for item in likes]

        # Normalize to lowercase and remove duplicates
        unique_likes = self._remove_duplicates([item.lower() for item in likes])

        # Remove items that have a prefix in the list
        simplified = self._remove_items_with_prefix(unique_likes)

        return simplified

    def _remove_duplicates(self, items: list) -> list:
        """Remove duplicate items while preserving order."""
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def _remove_items_with_prefix(self, items: list) -> list:
        """Remove items that start with another item in the list."""
        # Sort by length for efficient checking
        sorted_items = sorted(items, key=len)

        result = []
        for i, item in enumerate(sorted_items):
            # Check if this item starts with any shorter item
            if not any(item.startswith(other) for other in sorted_items[:i]):
                result.append(item)

        # Restore original order
        result_set = set(result)
        return [item for item in items if item in result_set]
