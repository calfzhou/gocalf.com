import pytest

from solution import Solution


@pytest.mark.parametrize('param, expected', [
    ([[1,2,3],[0,2],[0,1,3],[0,2]], False),
    ([[1,3],[0,2],[1,3],[0,2]], True),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, param, expected):
    assert sol.isBipartite(param) == expected
