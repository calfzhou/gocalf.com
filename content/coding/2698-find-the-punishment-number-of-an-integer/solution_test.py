import pytest

from solution import Solution


@pytest.mark.parametrize('n, expected', [
    (10, 182),
    (37, 1478),

    (35, 182),
    (36, 1478),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, expected):
    assert sol.punishmentNumber(n) == expected
