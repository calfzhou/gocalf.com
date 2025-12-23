import pytest

from solution import Solution


@pytest.mark.parametrize('nums, k, expected', [
    ([2,11,10,1,3], 10, 2),
    ([1,1,2,4,9], 20, 4),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, k, expected):
    assert sol.minOperations(nums.copy(), k) == expected
