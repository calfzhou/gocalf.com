import pytest

from solution import Solution


@pytest.mark.parametrize('values, expected', [
    ([8,1,5,2,6], 11),
    ([1,2], 2),

    ([1,3,5], 7),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, values, expected):
    assert sol.maxScoreSightseeingPair(values) == expected
