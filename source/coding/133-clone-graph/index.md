---
title: 133. Clone Graph
notebook: coding
tags:
- medium
date: 2024-11-10 15:35:08
updated: 2024-11-10 15:35:08
---
## Problem

Given a reference of a node in a **[connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph)** undirected graph.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

``` c++
class Node {
    public int val;
    public List<Node> neighbors;
}
```

**Test case format:**

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

**An adjacency list** is a collection of unordered **lists** used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

<https://leetcode.com/problems/clone-graph/>

**Example 1:**

{% invert %}
![case1](assets/133-clone-graph/case1.png)
{% endinvert %}

> Input: `adjList = [[2,4],[1,3],[2,4],[1,3]]`
> Output: `[[2,4],[1,3],[2,4],[1,3]]`
> Explanation: There are 4 nodes in the graph.
> 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
> 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
> 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
> 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

**Example 2:**

{% invert %}
![case2](assets/133-clone-graph/case2.png)
{% endinvert %}

> Input: `adjList = [[]]`
> Output: `[[]]`
> Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

**Example 3:**

> Input: `adjList = []`
> Output: `[]`
> Explanation: This an empty graph, it does not have any nodes.

**Constraints:**

- The number of nodes in the graph is in the range `[0, 100]`.
- `1 <= Node.val <= 100`
- `Node.val` is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

## Test Cases

``` python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
```

{% asset_code coding/133-clone-graph/solution_test.py %}

## Thoughts

写测试方法的时候相当于已经有解题的方法了。

核心就是遍历一遍 graph，确保找到所有的节点。图的遍历可以有深度优先或广度优先。

避免使用递归，可以用栈或队列缓存需要访问的节点，用循环替代递归。如果用栈（后进先出），相当于深度优先。如果用队列（先进先出），相当于广度优先。

可以用哈希表记录访问过的节点，key 是节点的 val，值是节点对象。也可以用数组，以 val 作为数组下标，只是需要动态扩大数组长度。

拿到所有节点之后，生成一组对应的新节点，并把每个新节点的 neighbors 设置好即可。

假设一共有 n 个节点，m 条边，则遍历所有节点和 clone 的时间复杂度都是 `O(n + m)`，空间复杂度为 `O(n + m)`。

## Code

{% asset_code coding/133-clone-graph/solution.py %}
