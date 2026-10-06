import pytest

from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3


@pytest.mark.parametrize('targetGrid, expected', [
    ([[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]], True),
    ([[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]], True),
    ([[1,2,1],[2,1,2],[1,2,1]], False),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2(), Solution3()])
def test_solution(sol, targetGrid, expected):
    assert sol.isPrintable(targetGrid.copy()) == expected
