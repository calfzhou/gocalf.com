import pytest

from solution import Solution


@pytest.mark.parametrize('nums, k, expected', [
    ([1,1,1,2,2,3], 2, [1,2]),
    ([1], 1, [1]),
])
class Test:
    def test_solution(self, nums, k, expected):
        sol = Solution()
        result = sol.topKFrequent(nums, k)
        assert sorted(result) == sorted(expected)
