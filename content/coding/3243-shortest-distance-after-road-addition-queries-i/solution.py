class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        sd = [n - i - 1 for i in range(n)]
        dests = [[i + 1] for i in range(n - 1)] # dests[i] is a list of cities which has direct road from city i.
        results = [1] * len(queries)
        for q, (u, v) in enumerate(queries):
            dests[u].append(v)
            if (d := sd[v] + 1) < sd[u]:
                sd[u] = d
                for i in range(u - 1, -1, -1):
                    sd[i] = min(sd[i], min(sd[j]+1 for j in dests[i] if j <= u))

            results[q] = sd[0]

        return results
