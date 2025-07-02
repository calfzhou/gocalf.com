import pytest

from solution import Solution


@pytest.mark.parametrize('text1, text2, expected', [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
])
class Test:
    def test_solution(self, text1, text2, expected):
        sol = Solution()
        assert sol.longestCommonSubsequence(text1, text2) == expected
