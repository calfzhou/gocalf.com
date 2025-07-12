import pytest

from solution import Solution


@pytest.mark.parametrize('s1, s2, expected', [
    ("bank", "kanb", True),
    ("attack", "defend", False),
    ("kelb", "kelb", True),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s1, s2, expected):
    assert sol.areAlmostEqual(s1, s2) == expected
