import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('s, t, expected', [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
])
class Test:
    def test_solution(self, s, t, expected):
        sol = Solution()
        assert sol.minWindow(s, t) == expected

    def test_solution2(self, s, t, expected):
        sol = Solution2()
        assert sol.minWindow(s, t) == expected
