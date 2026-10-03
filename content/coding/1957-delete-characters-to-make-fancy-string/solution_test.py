import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("leeetcode", "leetcode"),
    ("aaabaaaa", "aabaa"),
])
class Test:
    def test_solution(self, s, expected):
        sol = Solution()
        assert sol.makeFancyString(s) == expected
