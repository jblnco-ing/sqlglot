import unittest

from sqlglot.optimizer.simplify_likes import LikeSimplifier


class TestLikeSimplifier(unittest.TestCase):
    """Test cases for LikeSimplifier."""

    def test_empty_returns_empty(self):
        """Test that simplifying empty input returns empty."""
        simplifier = LikeSimplifier()
        result = simplifier.simplify([])
        self.assertEqual(result, [])

    def test_single_element_returns_same(self):
        """Test that simplifying a single element returns the same element."""
        simplifier = LikeSimplifier()
        result = simplifier.simplify(["neron"])
        self.assertEqual(result, ["neron"])

    def test_simplify_by_prefix(self):
        """Test that duplicate prefix patterns are simplified."""
        simplifier = LikeSimplifier()
        result = simplifier.simplify(["super", "superman"])
        self.assertEqual(result, ["super"])

    def test_simplify_by_prefix_reversed(self):
        """Test that prefix simplification works regardless of order."""
        simplifier = LikeSimplifier()
        result = simplifier.simplify(["superman", "super", "superheroe"])
        self.assertEqual(result, ["super"])


if __name__ == "__main__":
    unittest.main()
