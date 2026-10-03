import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('m, n, horizontalCut, verticalCut, expected', [
    (3, 2, [1,3], [5], 13),
    (2, 2, [7], [4], 15),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, m, n, horizontalCut, verticalCut, expected):
    assert sol.minimumCost(m, n, horizontalCut.copy(), verticalCut.copy()) == expected
