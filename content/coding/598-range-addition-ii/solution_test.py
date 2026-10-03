import pytest

from solution import Solution


@pytest.mark.parametrize('m, n, ops, expected', [
    (3, 3, [[2,2],[3,3]], 4),
    (3, 3, [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]], 4),
    (3, 3, [], 9),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, m, n, ops, expected):
    assert sol.maxCount(m, n, ops) == expected
