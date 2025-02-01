import pytest

from solution import Solution


@pytest.mark.parametrize('nums, target, expected', [
    ([2,5,6,0,0,1,2], 0, True),
    ([2,5,6,0,0,1,2], 3, False),

    ([1,0,1,1,1], 0, True),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, nums, target, expected):
    assert sol.search(nums, target) == expected
