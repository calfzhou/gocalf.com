import pytest

from solution import Solution


@pytest.mark.parametrize('numCourses, prerequisites, expected', [
    (2, [[1,0]], True),
    (2, [[1,0],[0,1]], False),

    (5, [[0,1],[0,2],[2,3],[2,4],[4,1]], True),
    (5, [[0,1],[0,2],[2,3],[2,4],[4,1],[1,2]], False),
])
class Test:
    def test_solution(self, numCourses, prerequisites, expected):
        sol = Solution()
        assert sol.canFinish(numCourses, prerequisites) == expected
