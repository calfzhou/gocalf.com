import pytest

from solution import Solution


@pytest.mark.parametrize('times, n, k, expected', [
    ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
    ([[1,2,1]], 2, 1, 1),
    ([[1,2,1]], 2, 2, -1),
])
class Test:
    def test_solution(self, times, n, k, expected):
        sol = Solution()
        assert sol.networkDelayTime(times, n, k) == expected
