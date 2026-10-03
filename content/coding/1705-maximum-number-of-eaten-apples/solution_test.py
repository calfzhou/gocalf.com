import pytest

from solution import Solution


@pytest.mark.parametrize('apples, days, expected', [
    ([1,2,3,5,2], [3,2,1,4,2], 7),
    ([3,0,0,0,0,2], [3,0,0,0,0,2], 5),

    ([9,2], [3,5], 5),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, apples, days, expected):
    assert sol.eatenApples(apples, days) == expected
