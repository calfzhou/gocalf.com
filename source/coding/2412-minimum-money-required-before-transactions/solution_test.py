import pytest

from solution import Solution


@pytest.mark.parametrize('transactions, expected', [
    ([[2,1],[5,0],[4,2]], 10),
    ([[3,0],[0,3]], 3),

    ([[7,2],[0,10],[5,0],[4,1],[5,8],[5,9]], 18),
])
@pytest.mark.parametrize('sol', [Solution()])
def test_solution(sol, transactions, expected):
    assert sol.minimumMoney(transactions) == expected
