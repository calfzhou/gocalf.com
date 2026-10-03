import pytest

from solution import Solution


@pytest.mark.parametrize('days, costs, expected', [
    ([1,4,6,7,8,20], [2,7,15], 11),
    ([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15], 17),

    ([1,4,6,7,8,20], [7,2,15], 6),
    ([1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29], [3,14,50], 50),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, days, costs, expected):
    assert sol.mincostTickets(days, costs.copy()) == expected
