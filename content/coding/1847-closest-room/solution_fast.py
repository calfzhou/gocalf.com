
from bisect import bisect_left, insort


class Solution:
    def closestRoom(self, rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
        k = len(queries)
        queries = [(q[0], q[1], j) for j, q in enumerate(queries)]
        queries.sort(key=lambda q: q[1], reverse=True)
        answer = [-1] * k

        n = len(rooms)
        rooms.sort(key=lambda r: r[1], reverse=True)
        valid_rooms = []

        i = 0
        for preferred, min_size, j in queries:
            while i < n and rooms[i][1] >= min_size:
                insort(valid_rooms, rooms[i][0])
                i += 1

            if valid_rooms:
                idx = bisect_left(valid_rooms, preferred)
                if idx == len(valid_rooms) or idx > 0 and preferred - valid_rooms[idx-1] <= valid_rooms[idx] - preferred:
                    idx -= 1
                answer[j] = valid_rooms[idx]

        return answer
