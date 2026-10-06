import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
])
class Test:
    def test_solution(self, s, expected):
        sol = Solution()
        assert sol.isPalindrome(s) == expected
