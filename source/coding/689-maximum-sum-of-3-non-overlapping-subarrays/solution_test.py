import pytest

from solution import Solution


@pytest.mark.parametrize('nums, k, expected', [
    ([1,2,1,2,6,7,5,1], 2, [0,3,5]),
    ([1,2,1,2,1,2,1,2,1], 2, [0,2,4]),

    ([6,9,9,1,1,1,1], 2, [0,2,4]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, k, expected):
    assert sol.maxSumOfThreeSubarrays(nums, k) == expected
