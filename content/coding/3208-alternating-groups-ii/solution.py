class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        cnt = 0
        length = 1
        for i in range(2-k, len(colors)):
            if colors[i] == colors[i-1]:
                length = 1
            elif length < k:
                length += 1
                if length == k:
                    cnt += 1
            else:
                cnt += 1

        return cnt
