import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    ([0,1], [[0,1],[1,0]]),
    ([1], [[1]]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sorted(sol.permute(nums)) == sorted(expected)
