import pytest

from solution import Solution


@pytest.mark.parametrize('arr, expected', [
    ([17,18,5,4,6,1], [18,6,6,6,1,-1]),
    ([400], [-1]),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, arr, expected):
    assert sol.replaceElements(arr.copy()) == expected
