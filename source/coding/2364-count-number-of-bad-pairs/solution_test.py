import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([4,1,3,3], 5),
    ([1,2,3,4,5], 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.countBadPairs(nums) == expected
