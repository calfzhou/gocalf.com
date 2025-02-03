import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,4,3,3,2], 2),
    ([3,3,3,3], 1),
    ([3,2,1], 3),

    ([1,9,7,1], 3),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.longestMonotonicSubarray(nums) == expected
