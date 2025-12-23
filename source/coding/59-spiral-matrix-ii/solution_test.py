import pytest

from solution import Solution


@pytest.mark.parametrize('n, expected', [
    (3, [[1,2,3],[8,9,4],[7,6,5]]),
    (1, [[1]]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, n, expected):
    assert sol.generateMatrix(n) == expected
