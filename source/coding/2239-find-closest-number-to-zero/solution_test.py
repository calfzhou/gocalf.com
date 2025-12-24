import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([-4,-2,1,4,8], 1),
    ([2,-1,1], 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.findClosestNumber(nums) == expected
