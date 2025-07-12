import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([18,43,36,13,7], 54),
    ([10,12,19,14], -1),

    ([279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128], 872),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.maximumSum(nums) == expected
