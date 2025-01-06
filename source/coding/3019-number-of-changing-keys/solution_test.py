import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("aAbBcC", 2),
    ("AaAaAaaA", 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    assert sol.countKeyChanges(s) == expected
