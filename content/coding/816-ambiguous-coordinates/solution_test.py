import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("(123)", ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]),
    ("(0123)", ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]),
    ("(00011)", ["(0, 0.011)","(0.001, 1)"]),

    ("(100)", ["(10, 0)"]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    assert sorted(sol.ambiguousCoordinates(s)) == sorted(expected)
