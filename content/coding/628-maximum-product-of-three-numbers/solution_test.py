import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], 6),
    ([1,2,3,4], 24),
    ([-1,-2,-3], -6),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.maximumProduct(nums) == expected
