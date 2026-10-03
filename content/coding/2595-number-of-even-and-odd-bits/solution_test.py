import pytest

from solution import Solution


@pytest.mark.parametrize('n, expected', [
    (50, [1,2]),
    (2, [0,1]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, expected):
    assert sol.evenOddBit(n) == expected
