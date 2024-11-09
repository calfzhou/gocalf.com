import pytest

from solution import Solution
from solution2 import Solution as Solution2

@pytest.mark.parametrize('s, expected', [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
])
class Test:
    def test_solution(self, s, expected):
        sol = Solution()
        assert sol.lengthOfLongestSubstring(s) == expected

    def test_solution2(self, s, expected):
        sol = Solution2()
        assert sol.lengthOfLongestSubstring(s) == expected
