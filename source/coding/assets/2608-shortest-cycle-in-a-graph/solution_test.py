import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('n, edges, expected', [
    (7, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]], 3),
    (4, [[0,1],[0,2]], -1),

    (8, [[1,3],[3,5],[5,7],[7,1],[0,2],[2,4],[4,0],[6,0],[6,1]], 3),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, n, edges, expected):
    assert sol.findShortestCycle(n, edges) == expected
