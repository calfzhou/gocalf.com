import pytest

from solution import Solution


def verify(res, nums):
    assert sorted(res) == sorted(nums)
    is_even = True
    for num in res:
        if is_even:
            if num & 1:
                is_even = False
        else:
            assert num & 1 == 1


@pytest.mark.parametrize('nums, expected', [
    ([3,1,2,4], [2,4,3,1]),
    ([0], [0]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    res = sol.sortArrayByParity(nums.copy())
    if res != expected:
        verify(res, nums)
