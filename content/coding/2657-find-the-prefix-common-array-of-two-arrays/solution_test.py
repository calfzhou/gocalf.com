import pytest

from solution import Solution


@pytest.mark.parametrize('a, b, expected', [
    ([1,3,2,4], [3,1,2,4], [0,2,3,4]),
    ([2,3,1], [3,1,2], [0,1,3]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, a, b, expected):
    assert sol.findThePrefixCommonArray(a, b) == expected
