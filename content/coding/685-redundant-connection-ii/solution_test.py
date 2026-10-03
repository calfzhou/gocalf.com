import pytest

from solution import Solution


@pytest.mark.parametrize('edges, expected', [
    ([[1,2],[1,3],[2,3]], [2,3]),
    ([[1,2],[2,3],[3,4],[4,1],[1,5]], [4,1]),

    ([[2,1],[3,1],[4,2],[1,4]], [2,1]),
    ([[5,2],[5,1],[3,1],[3,4],[3,5]], [3,1]),

    ([[4,1],[1,5],[4,2],[5,1],[4,3]], [5,1]),
    ([[3,4],[4,1],[1,2],[2,3],[5,1]], [4,1]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, edges, expected):
    assert sol.findRedundantDirectedConnection(edges) == expected
