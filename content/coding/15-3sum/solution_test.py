import pytest

from solution import Solution
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3


@pytest.mark.parametrize('nums, expected', [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),

    ([0,0,0,0,0,0,0], [[0,0,0]]),
    ([-1,-1,-1,-1,-1,0,0,0,0,1,1,1,1,1], [[-1,0,1],[0,0,0]]),

    ([-1,0,1,0], [[-1,0,1]]),
])
class Test:
    def test_solution(self, nums, expected):
        sol = Solution()
        res = sol.threeSum(nums)
        self._sort(res)
        self._sort(expected)
        assert res == expected

    def test_solution2(self, nums, expected):
        sol = Solution2()
        res = sol.threeSum(nums)
        self._sort(res)
        self._sort(expected)
        assert res == expected

    def test_solution3(self, nums, expected):
        sol = Solution3()
        res = sol.threeSum(nums)
        self._sort(res)
        self._sort(expected)
        assert res == expected

    def _sort(self, triplets: list[list[int]]):
        for triplet in triplets:
            triplet.sort()
        triplets.sort()
