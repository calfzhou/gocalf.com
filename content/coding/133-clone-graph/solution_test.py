from typing import Optional

import pytest

from node import Node
from solution import Solution


def build_graph(adjacencies: list[list[int]]) -> Optional['Node']:
    n = len(adjacencies)
    nodes = [Node(i + 1) for i in range(n)]
    for node, neighbors in zip(nodes, adjacencies):
        node.neighbors[:] = [nodes[j - 1] for j in neighbors]

    return nodes[0] if n > 0 else None


def get_adjacencies(node: Optional['Node']) -> list[list[int]]:
    if node is None:
        return []

    nodes: dict[int, Node] = {}
    visit_stack: list[Node] = []
    if node is not None:
        visit_stack.append(node)

    # depth-first by stack. To use breadth-first, try queue.
    while visit_stack:
        n1 = visit_stack.pop()
        if n1.val in nodes:
            continue
        nodes[n1.val] = n1
        visit_stack.extend(filter(lambda n2: n2.val not in nodes, n1.neighbors))

    return [[n2.val for n2 in nodes[i + 1].neighbors] for i in range(len(nodes))]


@pytest.mark.parametrize('adjacencies', [
    ([[2,4],[1,3],[2,4],[1,3]]),
    ([[]]),
    ([]),
])
class Test:
    def test_solution(self, adjacencies):
        node = build_graph(adjacencies)
        sol = Solution()
        res = sol.cloneGraph(node)

        if node is not None:
            assert res is not node

        actual = get_adjacencies(res)
        for neighbors in actual:
            neighbors.sort()

        assert actual == adjacencies
