import pytest

from solution import Solution


@pytest.mark.parametrize('prices, expected', [
    ([3,3,5,0,0,3,1,4], 6),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),

    ([2,4,1], 2),
    ([6,1,3,2,4,7], 7),
])
class Test:
    def test_solution(self, prices, expected):
        sol = Solution()
        assert sol.maxProfit(prices) == expected
