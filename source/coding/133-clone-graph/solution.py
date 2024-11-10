"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

from node import Node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        nodes: dict[int, 'Node'] = {}
        stack: list['Node'] = [node]

        # depth-first via stack.
        while stack:
            n1 = stack.pop()
            if n1.val in nodes:
                continue

            nodes[n1.val] = n1
            stack.extend(filter(lambda n2: n2.val not in nodes, n1.neighbors))

        n = len(nodes)
        cloned_nodes = [Node(i + 1) for i in range(n)]
        for cloned_n1 in cloned_nodes:
            n1 = nodes[cloned_n1.val]
            cloned_n1.neighbors[:] = [cloned_nodes[n2.val - 1] for n2 in n1.neighbors]

        return cloned_nodes[0]
