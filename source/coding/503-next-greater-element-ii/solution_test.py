import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,2,1], [2,-1,2]),
    ([1,2,3,4,3], [2,3,4,-1,4]),
])
@pytest.mark.parametrize('sol', [Solution()])
class Test:
    def test_solution(self, sol, nums, expected):
        assert sol.nextGreaterElements(nums) == expected
