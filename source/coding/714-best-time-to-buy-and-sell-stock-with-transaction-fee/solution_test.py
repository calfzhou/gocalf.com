import pytest

from solution import Solution


@pytest.mark.parametrize('prices, fee, expected', [
    ([1,3,2,8,4,9], 2, 8),
    ([1,3,7,5,10,3], 3, 6),
])
@pytest.mark.parametrize('sol', [Solution()])
class Test:
    def test_solution(self, sol, prices, fee, expected):
        assert sol.maxProfit(prices, fee) == expected
