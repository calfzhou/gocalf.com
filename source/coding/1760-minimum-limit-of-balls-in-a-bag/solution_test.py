import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, maxOperations, expected', [
    ([9], 2, 3),
    ([2,4,8,2], 4, 2),

    ([1,1,1], 2, 1),
])
class Test:
    def test_solution(self, nums, maxOperations, expected):
        sol = Solution()
        assert sol.minimumSize(nums, maxOperations) == expected

    def test_solution2(self, nums, maxOperations, expected):
        sol = Solution2()
        assert sol.minimumSize(nums, maxOperations) == expected
