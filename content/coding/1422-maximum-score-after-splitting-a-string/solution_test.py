import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("011101", 5),
    ("00111", 5),
    ("1111", 3),

    ("00", 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    assert sol.maxScore(s) == expected
