import pytest

from solution import Solution


@pytest.mark.parametrize('arr, expected', [
    ([1,2,2,6,6,6,6,7,10], 6),
    ([1,1], 1),

    ([5], 5),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, arr, expected):
    assert sol.findSpecialInteger(arr) == expected
