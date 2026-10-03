import pytest

from solution import Solution


def verify(res: str, nums: list[str]):
    assert res not in nums
    assert len(res) == len(nums[0])
    for d in res:
        assert d in '01'


@pytest.mark.parametrize('nums, expected', [
    (["01","10"], "11"),
    (["00","01"], "11"),
    (["111","011","001"], "101"),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    res = sol.findDifferentBinaryString(nums)
    if res != expected:
        verify(res, nums)
