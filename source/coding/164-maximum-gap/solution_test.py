import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([3,6,9,1], 3),
    ([10], 0),

    ([5,5], 0),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, expected):
    assert sol.maximumGap(nums) == expected
