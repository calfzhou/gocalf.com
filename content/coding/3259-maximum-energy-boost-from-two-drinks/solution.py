class Solution:
    def maxEnergyBoost(self, energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        n = len(energyDrinkA)
        ma = [0] * n
        mb = [0] * n
        for i in range(n):
            ma[i] = energyDrinkA[i] + max(ma[i-1], mb[i-2]) # Leverage Python's negative index behavior.
            mb[i] = energyDrinkB[i] + max(mb[i-1], ma[i-2])

        return max(ma[-1], mb[-1])
