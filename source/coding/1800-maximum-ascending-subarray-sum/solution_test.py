import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([10,20,30,5,10,50], 65),
    ([10,20,30,40,50], 150),
    ([12,17,15,13,10,11,12], 33),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.maxAscendingSum(nums) == expected
