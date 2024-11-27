import pytest

from solution import Solution


@pytest.mark.parametrize('c, expected', [
    (5, True),
    (3, False),

    (18, True),
])
class Test:
    def test_solution(self, c, expected):
        sol = Solution()
        assert sol.judgeSquareSum(c) == expected
