import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('nums, expected', [
    ([2,3,2], 4),
    ([5,5,5,5], 126),

    ([100,1,100,1,100], 0),
    ([1,2,3,4,5,6], 7),
    ([5,5], 21),
    ([7,5], 21),
    ([5,7], 21),
    ([5,7,5,7], 35),
    ([5,7,3,4,3], 1),
    ([5,8,3,4,3], 0),

    ([41,41,41,43,44,45,47,48,49,49], 777711786),
])
class Test:
    # def test_solution(self, nums, expected):
    #     sol = Solution()
    #     assert sol.countOfPairs(nums) == expected

    def test_solution2(self, nums, expected):
        sol = Solution2()
        assert sol.countOfPairs(nums) == expected
