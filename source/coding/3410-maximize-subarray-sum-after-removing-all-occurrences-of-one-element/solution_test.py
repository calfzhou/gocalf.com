import pytest

from solution import Solution
from solution_slow import Solution as SolutionSlow


@pytest.mark.parametrize('nums, expected', [
    ([-3,2,-2,-1,3,-2,3], 7),
    ([1,2,3,4], 10),

    ([-2,1,-3,4,-1,2,1,-5,4], 10),
    ([1], 1),
    ([5,4,-1,7,8], 24),
    ([-2,-2,-2], -2),
    ([1,-2,0,3], 4),
    ([1,-2,-2,3], 4),
    ([-50], -50),
])
@pytest.mark.parametrize('sol', [Solution(), SolutionSlow()])
def test_solution(sol, nums, expected):
    assert sol.maxSubarraySum(nums) == expected
