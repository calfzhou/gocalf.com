import pytest

from solution import Solution


@pytest.mark.parametrize('n, expected', [
    (4, False),
    (1, True),
    (2, True),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, expected):
    assert sol.canWinNim(n) == expected
