import pytest

from solution import Solution


@pytest.mark.parametrize('score, k, expected', [
    ([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2, [[7,5,11,2],[10,6,9,1],[4,8,3,15]]),
    ([[3,4],[5,6]], 0, [[5,6],[3,4]]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, score, k, expected):
    assert sol.sortTheStudents(score.copy(), k) == expected
