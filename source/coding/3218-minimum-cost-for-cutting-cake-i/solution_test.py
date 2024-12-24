import pytest

from solution import Solution


@pytest.mark.parametrize('m, n, horizontalCut, verticalCut, expected', [
    (3, 2, [1,3], [5], 13),
    (2, 2, [7], [4], 15),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, m, n, horizontalCut, verticalCut, expected):
    assert sol.minimumCost(m, n, horizontalCut, verticalCut) == expected
