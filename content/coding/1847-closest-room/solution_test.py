import pytest

from solution import Solution
from solution_fast import Solution as SolutionFast
from solution3 import Solution as Solution3


@pytest.mark.parametrize('rooms, queries, expected', [
    ([[2,2],[1,2],[3,2]], [[3,1],[3,3],[5,2]], [3,-1,3]),
    ([[1,4],[2,3],[3,5],[4,1],[5,2]], [[2,3],[2,4],[2,5]], [2,1,3]),

    (
        [[23,22],[6,20],[15,6],[22,19],[2,10],[21,4],[10,18],[16,1],[12,7],[5,22]],
        [[12,5],[15,15],[21,6],[15,1],[23,4],[15,11],[1,24],[3,19],[25,8],[18,6]],
        [12,10,22,15,23,10,-1,5,23,15]
    ),
])
class Test:
    def test_solution(self, rooms, queries, expected):
        sol = Solution()
        assert sol.closestRoom(rooms.copy(), queries.copy()) == expected

    def test_solution_fast(self, rooms, queries, expected):
        sol = SolutionFast()
        assert sol.closestRoom(rooms.copy(), queries.copy()) == expected

    def test_solution3(self, rooms, queries, expected):
        sol = Solution3()
        assert sol.closestRoom(rooms.copy(), queries.copy()) == expected
