import pytest

from solution import Solution


@pytest.mark.parametrize('k, prices, expected', [
    (2, [2,4,1], 2),
    (2, [3,2,6,5,0,3], 7),

    (2, [1], 0),
])
@pytest.mark.parametrize('sol', [Solution()])
class Test:
    def test_solution(self, sol, k, prices, expected):
        assert sol.maxProfit(k, prices) == expected
