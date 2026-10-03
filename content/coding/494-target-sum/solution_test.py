import pytest

from solution import Solution


@pytest.mark.parametrize('nums, target, expected', [
    ([1,1,1,1,1], 3, 5),
    ([1], 1, 1),

    ([1,0], 1, 2),
    ([30,1,5,32,16,17,30,29,48,14,29,4,31,12,40,13,13,20,41,38], 9, 6867),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, target, expected):
    assert sol.findTargetSumWays(nums, target) == expected
