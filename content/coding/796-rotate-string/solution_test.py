import pytest

from solution import Solution


@pytest.mark.parametrize('s, goal, expected', [
    ("abcde", "cdeab", True),
    ("abcde", "abced", False),
])
class Test:
    def test_solution(self, s, goal, expected):
        sol = Solution()
        assert sol.rotateString(s, goal) == expected
