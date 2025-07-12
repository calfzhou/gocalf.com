class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        n = len(events)

        events.sort(key=lambda e: e[0])
        max_ge_start = [[e[0], 0] for e in events] # (start time, max value)
        for i in range(-1, -n - 1, -1):
            max_ge_start[i][1] = max(max_ge_start[i+1][1], events[i][2])

        events.sort(key=lambda e: e[1])
        max_le_end = [[e[1], 0] for e in events] # (end time, max value)
        for i in range(n):
            max_le_end[i][1] = max(max_le_end[i-1][1], events[i][2])

        after = best = max_ge_start[0][1]
        before = 0
        i = j = 0
        while j < n:
            if i == n or max_ge_start[i][0] > max_le_end[j][0]:
                before = max_le_end[j][1]
                j += 1
            elif i < n:
                i += 1
                after = max_ge_start[i][1] if i < n else 0

            if after + before > best:
                best = after + before

        return best
