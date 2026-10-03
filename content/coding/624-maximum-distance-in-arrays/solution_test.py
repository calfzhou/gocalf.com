import pytest

from solution import Solution


@pytest.mark.parametrize('arrays, expected', [
    ([[1,2,3],[4,5],[1,2,3]], 4),
    ([[1],[1]], 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, arrays, expected):
    assert sol.maxDistance(arrays) == expected
