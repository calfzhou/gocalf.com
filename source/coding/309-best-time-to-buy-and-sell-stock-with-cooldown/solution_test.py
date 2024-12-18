import pytest

from solution import Solution


@pytest.mark.parametrize('prices, expected', [
    ([1,2,3,0,2], 3),
    ([1], 0),
])
@pytest.mark.parametrize('sol', [Solution()])
class Test:
    def test_solution(self, sol, prices, expected):
        assert sol.maxProfit(prices) == expected
