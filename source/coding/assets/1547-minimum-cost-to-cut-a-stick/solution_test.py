import pytest

from solution import Solution


@pytest.mark.parametrize('n, cuts, expected', [
    (7, [1,3,4,5], 16),
    (9, [5,6,1,4,2], 22),
])
class Test:
    def test_solution(self, n, cuts, expected):
        sol = Solution()
        assert sol.minCost(n, cuts) == expected
