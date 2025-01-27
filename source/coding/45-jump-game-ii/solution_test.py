import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,3,1,1,4], 2),
    ([2,3,0,1,4], 2),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.jump(nums) == expected
