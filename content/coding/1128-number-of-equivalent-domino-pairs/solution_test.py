import pytest

from solution import Solution


@pytest.mark.parametrize('dominoes, expected', [
    ([[1,2],[2,1],[3,4],[5,6]], 1),
    ([[1,2],[1,2],[1,1],[1,2],[2,2]], 3),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, dominoes, expected):
    assert sol.numEquivDominoPairs(dominoes) == expected
