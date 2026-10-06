import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, expected', [
    ([12,5,7,23], True),
    ([29,6,10], True),
    ([3,6], False),

    ([1], True),
    ([2], False),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, nums, expected):
    assert sol.isGoodArray(nums) == expected
