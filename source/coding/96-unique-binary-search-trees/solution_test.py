import pytest

from solution import Solution


@pytest.mark.parametrize('n, expected', [
    (3, 5),
    (1, 1),

    (5, 42),
    (19, 1767263190),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, expected):
    assert sol.numTrees(n) == expected
