class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        n = len(position)

        def check(force: int) -> bool:
            count = 1
            prev = position[0]
            for i in range(1, n):
                if position[i] - prev >= force:
                    prev = position[i]
                    count += 1

            return count >= m

        low = 1
        high = (position[-1] - position[0]) // (m - 1)
        while low <= high:
            mid = (low + high) >> 1
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
