import copy

import pytest

from solution import Solution
from solution2 import Solution as Solution2


@pytest.mark.parametrize('matrix, expected', [
    ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
    ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),

    ([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]], [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
])
class Test:
    def test_solution(self, matrix, expected):
        sol = Solution()
        matrix = copy.deepcopy(matrix)
        sol.setZeroes(matrix)
        assert matrix == expected

    def test_solution2(self, matrix, expected):
        sol = Solution2()
        matrix = copy.deepcopy(matrix)
        sol.setZeroes(matrix)
        assert matrix == expected
