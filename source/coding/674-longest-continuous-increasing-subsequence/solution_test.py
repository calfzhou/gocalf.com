import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,3,5,4,7], 3),
    ([2,2,2,2,2], 1),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.findLengthOfLCIS(nums) == expected
