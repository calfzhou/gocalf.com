import pytest

from solution import Solution


@pytest.mark.parametrize('graph, expected', [
    ([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]], 0),
    ([[1,3],[0],[3],[0,2]], 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, graph, expected):
    assert sol.catMouseGame(graph) == expected
