
from bisect import bisect_right

gt = lambda a, b: a > b
lt = lambda a, b: a < b


class Solution:
    def closestRoom(self, rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
        rooms.sort() # Sort rooms by roomId.
        queries = [(q[0], q[1], j) for j, q in enumerate(queries)] # Remember origin query index before sort.
        queries.sort() # Sort queries by preferred.
        answer = [-1] * len(queries)

        for done, valid in enumerate((gt, lt)):
            j = len(queries) - 1
            while j >= 0 and valid(queries[j][0], rooms[-1][0]): # Skip no-result queries for current direction.
                j -= 1

            stack = []
            for i in range(len(rooms) - 1, -1, -1):
                size = rooms[i][1]
                while stack and rooms[stack[-1]][1] <= size:
                    stack.pop()
                stack.append(i)

                while j >= 0 and (i == 0 or valid(queries[j][0], rooms[i-1][0])):
                    preferred, min_size, qid = queries[j]
                    j -= 1
                    if answer[qid] == preferred: continue

                    idx = bisect_right(stack, -min_size, key=lambda x: -rooms[x][1]) - 1
                    if idx < 0: continue
                    if answer[qid] == -1 or preferred - rooms[stack[idx]][0] <= answer[qid] - preferred:
                        answer[qid] = rooms[stack[idx]][0]

            if done: break
            rooms.reverse()
            queries.reverse()

        return answer
