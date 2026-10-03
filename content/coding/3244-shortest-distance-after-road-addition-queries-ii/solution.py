class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        f = [i+1 for i in range(n)] # f[i] == n means i was removed.
        dis = n - 1
        results = [dis] * len(queries)
        for q, (u, v) in enumerate(queries):
            if (i := f[u]) < v:
                f[u] = v
                while i < v:
                    f[i], i = n, f[i]
                    dis -= 1 # City `i` removed.

            results[q] = dis

        return results
