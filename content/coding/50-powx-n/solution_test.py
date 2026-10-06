import pytest

from solution import Solution


@pytest.mark.parametrize('x, n, expected', [
    (2.00000, 10, 1024.00000),
    (2.10000, 3, 9.26100),
    (2.00000, -2, 0.25000),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, x, n, expected):
    assert sol.myPow(x, n) == pytest.approx(expected, abs=1e-6)
