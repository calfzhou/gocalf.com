import pytest

from solution import Solution


@pytest.mark.parametrize('edges, coins, k, expected', [
    ([[0,1],[1,2],[2,3]], [10,10,3,3], 5, 11),
    ([[0,1],[0,2]], [8,4,4], 0, 16),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, edges, coins, k, expected):
    assert sol.maximumPoints(edges, coins, k) == expected
