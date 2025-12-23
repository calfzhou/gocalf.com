import pytest

from solution import Solution


@pytest.mark.parametrize('intervals, expected', [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),

    ([[1,4],[0,4]], [[0,4]]),
    ([[1,4],[2,3]], [[1,4]])
])
class Test:
    def test_solution(self, intervals, expected):
        sol = Solution()
        assert sol.merge(intervals) == expected
