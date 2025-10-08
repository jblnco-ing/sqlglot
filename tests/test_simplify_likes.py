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

    def test_simplify_two_different_prefixes(self):
        """Test prefix simplification with two different prefix groups."""
        simplifier = LikeSimplifier()
        result = simplifier.simplify(["batman", "bat", "spider", "spiderman"])
        self.assertEqual(result, ["bat", "spider"])

    def test_remove_exact_duplicates(self):
        """Test that exact duplicates are removed."""
        simplifier = LikeSimplifier()
        result = simplifier.simplify(["batman", "robin", "batman"])
        self.assertEqual(result, ["batman", "robin"])

    def test_case_insensitive_prefix(self):
        """Test that prefix matching ignores case and returns lowercase."""
        simplifier = LikeSimplifier()
        result = simplifier.simplify(["SUPER", "superman"])
        self.assertEqual(result, ["super"])


if __name__ == "__main__":
    unittest.main()
