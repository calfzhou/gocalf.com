from typing import List


class Stat:
    def __init__(self, val: int):
        self.val = val
        self.node_count = 1
        self.good_count = 0
        self.good = True
        self.child_node_count: int|None = None


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        nodes = [set() for _ in range(n)] # nodes[i]: its neighbors (parent and children).
        for i, j in edges:
            nodes[i].add(j)
            nodes[j].add(i)

        stats = [Stat(None)]
        tasks = [(0, False)]
        while tasks:
            r, ready = tasks.pop()
            node = Stat(r)
            parent = stats[-1]
            if ready:
                node = stats.pop()
                parent = stats[-1]
            elif r == 0 or len(nodes[r]) > 1: # Non-leaf.
                tasks.append((r, True))
                for c in filter(lambda i: i != parent.val, nodes[r]):
                    tasks.append((c, False))
                stats.append(node)
                continue

            node.good_count += 1 if node.good else 0
            parent.node_count += node.node_count
            parent.good_count += node.good_count
            if parent.child_node_count is not None and node.node_count != parent.child_node_count:
                parent.good = False
            parent.child_node_count = node.node_count

        return stats[0].good_count
