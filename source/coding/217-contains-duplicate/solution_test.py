import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.containsDuplicate(nums) == expected
