import pytest

from solution import Solution


@pytest.mark.parametrize('numCourses, prerequisites, queries, expected', [
    (2, [[1,0]], [[0,1],[1,0]], [False, True]),
    (2, [], [[1,0],[0,1]], [False, False]),
    (3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]], [True, True]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, numCourses, prerequisites, queries, expected):
    assert sol.checkIfPrerequisite(numCourses, prerequisites, queries) == expected
