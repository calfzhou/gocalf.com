import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([10,4,-8,7], 2),
    ([2,3,1,0], 2),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.waysToSplitArray(nums) == expected
