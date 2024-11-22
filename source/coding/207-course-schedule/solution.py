class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph: list[list[int]] = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        status = [0] * numCourses # 0: unknown; 1: processing; 2: finished.
        for i in range(numCourses):
            if status[i] == 2:
                continue

            stack = [i]
            while stack:
                u = stack.pop()
                if status[u] == 1:
                    status[u] = 2
                    continue

                status[u] = 1
                stack.append(u)
                for v in graph[u]:
                    if status[v] == 1:
                        return False
                    elif status[v] == 0:
                        stack.append(v)

        return True
