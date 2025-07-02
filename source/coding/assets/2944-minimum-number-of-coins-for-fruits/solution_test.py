import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('prices, expected', [
    ([3,1,2], 4),
    ([1,10,1,1], 2),
    ([26,18,6,12,49,7,45,45], 39),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, prices, expected):
    assert sol.minimumCoins(prices.copy()) == expected
