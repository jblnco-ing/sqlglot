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


if __name__ == "__main__":
    unittest.main()
