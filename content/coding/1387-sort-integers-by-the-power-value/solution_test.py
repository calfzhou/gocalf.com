import pytest

from solution import Solution


@pytest.mark.parametrize('lo, hi, k, expected', [
    (12, 15, 2, 13),
    (7, 11, 4, 7),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, lo, hi, k, expected):
    assert sol.getKth(lo, hi, k) == expected
