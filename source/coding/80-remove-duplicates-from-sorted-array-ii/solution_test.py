import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected, expectedNums', [
    ([1,1,1,2,2,3], 5, [1,1,2,2,3]),
    ([0,0,1,1,1,1,2,3,3], 7, [0,0,1,1,2,3,3]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected, expectedNums):
    nums = nums.copy()
    assert sol.removeDuplicates(nums) == expected
    assert nums[:expected] == expectedNums
