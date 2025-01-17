import pytest

from solution import Solution


@pytest.mark.parametrize('nums, k, expected', [
    ([1,2,3], 2, 1),
    ([2,1,8], 10, 3),
    ([1,2], 0 ,1),

    ([1,2,4,8], 16, -1)
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, k, expected):
    assert sol.minimumSubarrayLength(nums.copy(), k) == expected
