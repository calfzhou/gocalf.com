import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,1,2,2,3,4], True),
    ([1,1,1,1], False),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.isPossibleToSplit(nums) == expected
