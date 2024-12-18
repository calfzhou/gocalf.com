import pytest

from solution import Solution
from solution_nlogn import Solution as SolutionNlogn
from solution_n import Solution as SolutionN


@pytest.mark.parametrize('prices, expected', [
    ([8,4,6,2,3], [4,2,4,2,3]),
    ([1,2,3,4,5], [1,2,3,4,5]),
    ([10,1,1,6], [9,0,1,6]),
])
@pytest.mark.parametrize('sol', [Solution(), SolutionNlogn(), SolutionN()])
class Test:
    def test_solution(self, sol, prices, expected):
        assert sol.finalPrices(prices.copy()) == expected
