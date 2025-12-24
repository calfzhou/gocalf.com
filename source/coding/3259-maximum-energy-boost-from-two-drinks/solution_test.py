import pytest

from solution import Solution


@pytest.mark.parametrize('energyDrinkA, energyDrinkB, expected', [
    ([1,3,1], [3,1,1], 5),
    ([4,1,1], [1,1,3], 7),

    ([5,5,6,3,4,3,3,4], [5,3,3,4,4,6,6,3], 35),
])
class Test:
    def test_solution(self, energyDrinkA, energyDrinkB, expected):
        sol = Solution()
        assert sol.maxEnergyBoost(energyDrinkA, energyDrinkB) == expected
