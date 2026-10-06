import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, expected', [
    ([1,-3,2,3,-4], 5),
    ([2,-5,1,-4,3,-2], 8),

    ([-3,-5,-3,-2,-6,3,10,-10,-8,-3,0,10,3,-5,8,7,-9,-9,5,-8], 27),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, nums, expected):
    assert sol.maxAbsoluteSum(nums) == expected
