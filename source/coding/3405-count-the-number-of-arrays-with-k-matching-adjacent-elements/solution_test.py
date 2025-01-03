import pytest

from solution import Solution


@pytest.mark.parametrize('n, m, k, expected', [
    (3, 2, 1, 4),
    (4, 2, 2, 6),
    (5, 2, 0, 2),

    (1, 1, 0, 1),
    (63556, 90183, 30596, 417830506),
    (68450, 16745, 60839, 418664322),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, m, k, expected):
    res = sol.countGoodArrays(n, m, k)
    assert type(res) == int and res == expected
