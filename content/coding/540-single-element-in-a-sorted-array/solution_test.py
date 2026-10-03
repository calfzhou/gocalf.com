import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,1,2,3,3,4,4,8,8], 2),
    ([3,3,7,7,10,11,11], 10),

    ([6], 6),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.singleNonDuplicate(nums) == expected
