import pytest

from solution import Solution


@pytest.mark.parametrize('s, expected', [
    ("abba", 2),
    ("cdef", 4),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, s, expected):
    assert sol.minAnagramLength(s) == expected
