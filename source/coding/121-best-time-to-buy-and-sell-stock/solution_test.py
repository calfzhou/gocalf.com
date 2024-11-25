import pytest

from solution import Solution


@pytest.mark.parametrize('prices, expected', [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),

    ([1,2], 1),
])
class Test:
    def test_solution(self, prices, expected):
        sol = Solution()
        assert sol.maxProfit(prices) == expected
