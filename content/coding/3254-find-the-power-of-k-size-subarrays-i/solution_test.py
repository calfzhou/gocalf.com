import pytest

from solution import Solution


@pytest.mark.parametrize('nums, k, expected', [
    ([1,2,3,4,3,2,5], 3, [3,4,-1,-1,-1]),
    ([2,2,2,2,2], 4, [-1,-1]),
    ([3,2,3,2,3,2], 2, [-1,3,-1,3,-1]),

    ([1], 1, [1]),
    ([6], 1, [6]),
])
class Test:
    def test_solution(self, nums, k, expected):
        sol = Solution()
        assert sol.resultsArray(nums, k) == expected
