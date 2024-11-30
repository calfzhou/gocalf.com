from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next = str(self.next.val) if self.next else 'X'
        return f'{self.val} -> {next}'


class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        graph: dict[int, list[int]] = defaultdict(list) # vertex: list of its successor.
        degrees: dict[int, int] = defaultdict(int) # vertex: its (out-degree) - (in-degree).
        for u, v in pairs:
            graph[u].append(v)
            degrees[u] += 1
            degrees[v] -= 1

        u0 = next((u for u, d in degrees.items() if d == 1), pairs[0][0])
        root = ListNode(u0) # Root of the full Eulerian trail.
        indexes = {u0: root} # vertex: one of its occurrence in Eulerian trail.
        u = u0
        while u is not None:
            node = indexes[u]
            further = node.next

            # Find a trail starting from u.
            while u in graph:
                vs = graph[u]
                v = vs.pop()
                node.next = node = indexes[v] = ListNode(v)
                if not vs:
                    del graph[u]

                u = v

            node.next = further
            u = next((u for u in graph if u in indexes), None)

        result = [None] * len(pairs)
        node = root
        i = 0
        while node.next:
            result[i] = [node.val, node.next.val]
            node = node.next
            i += 1

        return result
