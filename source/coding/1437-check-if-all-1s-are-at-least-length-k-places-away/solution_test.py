import pytest

from solution import Solution


@pytest.mark.parametrize('nums, k, expected', [
    ([1,0,0,0,1,0,0,1], 2, True),
    ([1,0,0,1,0,1], 2, False),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, k, expected):
    assert sol.kLengthApart(nums, k) == expected
