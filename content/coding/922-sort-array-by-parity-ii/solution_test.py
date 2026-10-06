import pytest

from solution import Solution


def verify(res, nums):
    assert sorted(res) == sorted(nums)
    assert all([i % 2 == 0 for i in res[::2]])
    assert all([i % 2 != 0 for i in res[1::2]])


@pytest.mark.parametrize('nums, expected', [
    ([4,2,5,7], [4,5,2,7]),
    ([2,3], [2,3]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    res = sol.sortArrayByParityII(nums.copy())
    if res != expected:
        verify(res, nums)
