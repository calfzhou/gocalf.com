class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        result = []
        for i in range(len(height) - 1):
            if height[i] > threshold:
                result.append(i + 1)

        return result
