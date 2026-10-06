import pytest

from solution import Solution


@pytest.mark.parametrize('coins, amount, expected', [
    ([1,2,5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),

    ([1,2,4,5], 12, 3),
    ([1,60,100], 120, 2),

    ([186,419,83,408], 6249, 20),
    ([411,412,413,414,415,416,417,418,419,420,421,422], 9864, 24),
    ([2147483647], 2, -1),
])
class Test:
    def test_solution(self, coins, amount, expected):
        sol = Solution()
        assert sol.coinChange(coins, amount) == expected
