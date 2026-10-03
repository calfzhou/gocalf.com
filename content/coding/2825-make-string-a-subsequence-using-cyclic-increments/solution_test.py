import pytest

from solution import Solution


@pytest.mark.parametrize('str1, str2, expected', [
    ("abc", "ad", True),
    ("zc", "ad", True),
    ("ab", "d", False),
])
class Test:
    def test_solution(self, str1, str2, expected):
        sol = Solution()
        assert sol.canMakeSubsequence(str1, str2) == expected
