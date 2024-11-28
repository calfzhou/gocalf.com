import pytest

from solution import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,3,2], 4),
    ([5,5,5,5], 126),

    ([100,1,100,1,100], 0),
    ([1,2,3,4,5,6], 7),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        assert sol.countOfPairs(nums) == expected
