from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = [0] * 121
        for age in ages:
            counts[age] += 1

        for age in range(1, len(counts)):
            counts[age] += counts[age - 1]

        total = 0
        for age_x in range(1, len(counts)):
            count_x = counts[age_x] - counts[age_x - 1]
            if count_x == 0:
                continue

            exclude_age_y = (age_x >> 1) + 7
            if age_x < exclude_age_y + 1:
                continue

            count_y = counts[age_x] - counts[exclude_age_y] - 1 # Exclude himself.
            total += count_x * count_y

        return total
