---
title: 417. Pacific Atlantic Water Flow
notebook: coding
tags:
- medium
date: 2024-11-16 00:36:11
updated: 2024-11-16 00:36:11
---
## Problem

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return _a **2D list** of grid coordinates_ `result` _where_ `result[i] = [ri, ci]` _denotes that rain water can flow from cell_ `(ri, ci)` _to **both** the Pacific and Atlantic oceans_.

<https://leetcode.com/problems/pacific-atlantic-water-flow/>

**Example 1:**

![case1](assets/417-pacific-atlantic-water-flow/case1.png)

> Input: `heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]`
> Output: `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`
> Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
>
> ``` text
> [0,4]: [0,4] -> Pacific Ocean
> [0,4] -> Atlantic Ocean
> [1,3]: [1,3] -> [0,3] -> Pacific Ocean
> [1,3] -> [1,4] -> Atlantic Ocean
> [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
> [1,4] -> Atlantic Ocean
> [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
> [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
> [3,0]: [3,0] -> Pacific Ocean
> [3,0] -> [4,0] -> Atlantic Ocean
> [3,1]: [3,1] -> [3,0] -> Pacific Ocean
> [3,1] -> [4,1] -> Atlantic Ocean
> [4,0]: [4,0] -> Pacific Ocean
> [4,0] -> Atlantic Ocean
> ```
>
> Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

**Example 2:**

> Input: `heights = [[1]]`
> Output: `[[0,0]]`
> Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

**Constraints:**

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10⁵`

## Test Cases

``` python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
```

{% asset_code coding/assets/417-pacific-atlantic-water-flow/solution_test.py %}

## Thoughts

构造一个有 `m * n + 2` 个节点的有向图（可能有环），前 `m * n` 个节点对应 island 的每个 cell，最后两个节点分别对应太平洋（PO）和大西洋（AO）。

图中的有向边，表示从终点对应的 cell 可以流到起点对应的 cell（或海洋）。因为比较稀疏，可以用邻接表的存储方式。

从太平洋对应的节点出发，遍历所有可达的 cells。可以用栈辅助做深度优先遍历。然后也找出从大西洋可达的所有 cells。二者的交集就是结果。

时间和空间复杂度都是 `O(m * n)`。

## Code

{% asset_code coding/assets/417-pacific-atlantic-water-flow/solution.py %}
