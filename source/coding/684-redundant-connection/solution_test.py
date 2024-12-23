import pytest

from solution import Solution



@pytest.mark.parametrize('edges, expected', [
    ([[1,2],[1,3],[2,3]], [2,3]),
    ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4]),

    ([[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]], [4,10])
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, edges, expected):
    result = sol.findRedundantConnection(edges)
    assert result == expected
