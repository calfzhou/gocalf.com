import pytest

from solution import Solution


@pytest.mark.parametrize('low, high, zero, one, expected', [
    (3, 3, 1, 1, 8),
    (2, 3, 1, 2, 5),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, low, high, zero, one, expected):
    assert sol.countGoodStrings(low, high, zero, one) == expected
