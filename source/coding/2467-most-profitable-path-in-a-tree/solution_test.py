import pytest

from solution import Solution


@pytest.mark.parametrize('edges, bob, amount, expected', [
    ([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6], 6),
    ([[0,1]], 1, [-7280,2350], -7280),

    ([[0,1],[1,2],[2,3]], 3, [-5644,-6018,1188,-8502], -11662),
    ([[0,2],[0,5],[1,3],[1,5],[2,4]], 4, [5018,8388,6224,3466,3808,3456], 20328),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, edges, bob, amount, expected):
    assert sol.mostProfitablePath(edges, bob, amount.copy()) == expected
