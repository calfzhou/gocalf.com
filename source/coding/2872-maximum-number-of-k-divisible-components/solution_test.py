import pytest

from solution import Solution


@pytest.mark.parametrize('n, edges, values, k, expected', [
    (5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6, 2),
    (7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3, 3),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, edges, values, k, expected):
    assert sol.maxKDivisibleComponents(n, edges, values.copy(), k) == expected
