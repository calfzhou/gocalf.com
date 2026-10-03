import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, expected', [
    ([1,1,1,1,1,1], 6),
    ([1,2,2,3,3,4], 4),
    ([0,1,2,3,4,5,6,7,8], 0),

    ([0,1,0,1,-1], 0),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
def test_solution(sol, nums, expected):
    assert sol.subsequencesWithMiddleMode(nums) == expected
