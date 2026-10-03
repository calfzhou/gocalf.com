import pytest

from solution import Solution


@pytest.mark.parametrize('intervals, expected', [
    ([[1,2]], [-1]),
    ([[3,4],[2,3],[1,2]], [-1,0,1]),
    ([[1,4],[2,3],[3,4]], [-1,2,-1]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, intervals, expected):
    assert sol.findRightInterval(intervals) == expected
