import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, expected', [
    ([1,2,1], [2,-1,2]),
    ([1,2,3,4,3], [2,3,4,-1,4]),
])
@pytest.mark.parametrize('sol', [Solution(), Solution2()])
class Test:
    def test_solution(self, sol, nums, expected):
        assert sol.nextGreaterElements(nums) == expected
