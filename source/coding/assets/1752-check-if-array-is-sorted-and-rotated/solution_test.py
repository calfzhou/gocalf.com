import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([3,4,5,1,2], True),
    ([2,1,3,4], False),
    ([1,2,3], True),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.check(nums) == expected
