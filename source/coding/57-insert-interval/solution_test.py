import pytest

from solution import Solution


@pytest.mark.parametrize('intervals, newInterval, expected', [
    ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),

    ([[5,7],[8,10]], [2,3], [[2,3],[5,7],[8,10]]),
    ([[5,7],[8,10]], [2,5], [[2,7],[8,10]]),
    ([[5,7],[8,10]], [2,12], [[2,12]]),
    ([[5,6],[9,10]], [7,8], [[5,6],[7,8],[9,10]]),

    ([[4,4],[5,7],[8,10]], [10,18], [[4,4],[5,7],[8,18]])
])
class Test:
    def test_solution(self, intervals, newInterval, expected):
        sol = Solution()
        assert sol.insert(intervals, newInterval) == expected
