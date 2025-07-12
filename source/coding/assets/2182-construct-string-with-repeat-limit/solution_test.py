import pytest

from solution import Solution


@pytest.mark.parametrize('s, repeatLimit, expected', [
    ("cczazcc", 3, "zzcccac"),
    ("aababab", 2, "bbabaa"),
])
class Test:
    def test_solution(self, s, repeatLimit, expected):
        sol = Solution()
        assert sol.repeatLimitedString(s, repeatLimit) == expected
