import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected, expectedNums', [
    ([1,1,2], 2, [1,2]),
    ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected, expectedNums):
    nums = nums.copy()
    assert sol.removeDuplicates(nums) == expected
    assert nums[:expected] == expectedNums
