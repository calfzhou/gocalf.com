import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,1,4,3], 2),
    ([2,4,1,3], 3),
    ([1,3,4,2,5], 0),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.semiOrderedPermutation(nums) == expected
