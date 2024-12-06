import pytest

from solution import Solution


@pytest.mark.parametrize('banned, n, maxSum, expected', [
    ([1,6,5], 5, 6, 2),
    ([1,2,3,4,5,6,7], 8, 1, 0),
    ([11], 7, 50, 7),
])
class Test:
    def test_solution(self, banned, n, maxSum, expected):
        sol = Solution()
        assert sol.maxCount(banned, n, maxSum) == expected
