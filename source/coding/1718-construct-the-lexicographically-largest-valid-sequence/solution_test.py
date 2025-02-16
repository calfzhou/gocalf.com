import pytest

from solution import Solution


@pytest.mark.parametrize('n, expected', [
    (3, [3,1,2,3,2]),
    (5, [5,3,1,4,3,5,2,4,2]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, expected):
    assert sol.constructDistancedSequence(n) == expected
