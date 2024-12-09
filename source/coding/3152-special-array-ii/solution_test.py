import pytest

from solution import Solution


@pytest.mark.parametrize('nums, queries, expected', [
    ([3,4,1,2,6], [[0,4]], [False]),
    ([4,3,1,6], [[0,2],[2,3]], [False,True]),

    ([3,4,1,2,6], [[3,4]], [False]),
])
class Test:
    def test_solution(self, nums, queries, expected):
        sol = Solution()
        assert sol.isArraySpecial(nums, queries) == expected
