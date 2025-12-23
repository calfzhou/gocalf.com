---
title: 2097. Valid Arrangement of Pairs
notebook: coding
tags:
- hard
- todo
date: 2024-11-30 15:07:50
updated: 2024-11-30 15:07:50
---
## Problem

You are given a **0-indexed** 2D integer array `pairs` where `pairs[i] = [startᵢ, endᵢ]`. An arrangement of `pairs` is **valid** if for every index `i` where `1 <= i < pairs.length`, we have `endᵢ₋₁ == startᵢ`.

Return _**any** valid arrangement of_ `pairs`.

**Note:** The inputs will be generated such that there exists a valid arrangement of `pairs`.

<https://leetcode.com/problems/valid-arrangement-of-pairs/>

**Example 1:**

> Input: `pairs = [[5,1],[4,5],[11,9],[9,4]]`
> Output: `[[11,9],[9,4],[4,5],[5,1]]`
> Explanation:
> This is a valid arrangement since endᵢ₋₁ always equals startᵢ.
> end₀ = 9 == 9 = start₁
> end₁ = 4 == 4 = start₂
> end₂ = 5 == 5 = start₃

**Example 2:**

> Input: `pairs = [[1,3],[3,2],[2,1]]`
> Output: `[[1,3],[3,2],[2,1]]`
> Explanation:
> This is a valid arrangement since endᵢ₋₁ always equals startᵢ.
> end₀ = 3 == 3 = start₁
> end₁ = 2 == 2 = start₂
> The arrangements `[[2,1],[1,3],[3,2]]` and `[[3,2],[2,1],[1,3]]` are also valid.

**Example 3:**

> Input: `pairs = [[1,2],[1,3],[2,1]]`
> Output: `[[1,2],[2,1],[1,3]]`
> Explanation:
> This is a valid arrangement since endᵢ₋₁ always equals startᵢ.
> end₀ = 2 == 2 = start₁
> end₁ = 1 == 1 = start₂

**Constraints:**

- `1 <= pairs.length <= 10⁵`
- `pairs[i].length == 2`
- `0 <= startᵢ, endᵢ <= 10⁹`
- `startᵢ != endᵢ`
- No two pairs are exactly the same.
- There **exists** a valid arrangement of `pairs`.

## Test Cases

``` python
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
```

{% asset_code coding/assets/2097-valid-arrangement-of-pairs/solution_test.py %}

## Thoughts

以每个数字作为顶点，对于 `pairs[i] = [startᵢ, endᵢ]`，作 `startᵢ` 到 `endᵢ` 的有向边，构成有向图。

显然题目所求就是图中的欧拉通路。也就是「一笔画」问题。

> 欧拉通路：通过图中所有边一次且仅一次行遍所有顶点的通路。
>
> A directed graph has an Eulerian trail if and only if at most one vertex has `(out-degree) − (in-degree) = 1`, at most one vertex has `(in-degree) − (out-degree) = 1`, every other vertex has equal in-degree and out-degree. \[[wiki](https://en.wikipedia.org/wiki/Eulerian_path)\]

求欧拉通路一般有两个算法：[Fleury's algorithm](https://en.wikipedia.org/wiki/Eulerian_path#Fleury's_algorithm) 和 [Hierholzer's algorithm](https://en.wikipedia.org/wiki/Eulerian_path#Hierholzer's_algorithm)，后者效率要高得多。

用 Hierholzer 算法。

首先如果存在 `(out-degree) − (in-degree) = 1` 和 `(in-degree) − (out-degree) = 1` 的顶点，记为 `u₀` 和 `v₀`。它俩是欧拉通路的起点和终点。如果不存在，则有欧拉回路，可以从任何顶点断开得到欧拉通路。

如果存在 `u₀` 则取它，否则任取一个顶点 `u`，出发遍历图，每经过一条边就从边集中删除，直到遍历到某个顶点没有任何出边。显然如果是从 `u₀` 出发，最后一定会停在 `v₀`，否则一定会回到 `u`。

如果没有剩余的边了，则已经得到了欧拉通路（或回路）。否则看已有路径中的每个顶点，一定存在某个顶点有不在当前路径的边，从这个顶点（记为 `u'`）出发，直到再次回到 `u'`。把新得到的回路加入到原来的路径中，即 `u -> 原路径前半段 -> u' -> 刚找到的回路 -> u' -> 原路径后半段 -> u`。

图的存储用邻接表法，也便于遍历的时候删除访问过的边。整个邻接表用哈希表记录，当一个顶点的所有出边都处理完，可以将该顶点删除，以便快速判断是否还有未访问到的边。用链表记录已经找到的通路，以便可以和之后找到的回路合并。再用一个字典索引当前通路中各个顶点所在的链表节点，以便快速找到新回路的接入位置。

时间复杂度 `O(E)`，`E` 是图中边的数量，即 `pairs` 的长度。

## Code

{% asset_code coding/assets/2097-valid-arrangement-of-pairs/solution.py %}

空间消耗还好，运行速度不是很快，回头再优化【TODO】
