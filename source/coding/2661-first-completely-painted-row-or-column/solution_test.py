import pytest

from solution import Solution


@pytest.mark.parametrize('arr, mat, expected', [
    ([1,3,4,2], [[1,4],[2,3]], 2),
    ([2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]], 3),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, arr, mat, expected):
    assert sol.firstCompleteIndex(arr, mat) == expected
