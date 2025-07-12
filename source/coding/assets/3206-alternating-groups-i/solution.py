class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        cnt = 0
        for i in range(len(colors)):
            if colors[i-2] != colors[i-1] and colors[i-1] != colors[i]:
                cnt += 1

        return cnt
