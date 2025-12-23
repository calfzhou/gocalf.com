---
title: 3244. Shortest Distance After Road Addition Queries II
notebook: coding
tags:
- hard
date: 2024-11-20 11:32:39
updated: 2024-11-20 11:32:39
---
## Problem

You are given an integer `n` and a 2D integer array `queries`.

There are `n` cities numbered from `0` to `n - 1`. Initially, there is a **unidirectional** road from city `i` to city `i + 1` for all `0 <= i < n - 1`.

`queries[i] = [uᵢ, vᵢ]` represents the addition of a new **unidirectional** road from city `uᵢ` to city `vᵢ`. After each query, you need to find the **length** of the **shortest path** from city `0` to city `n - 1`.

There are no two queries such that `queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]`.

Return an array `answer` where for each `i` in the range `[0, queries.length - 1]`, `answer[i]` is the _length of the shortest path_ from city `0` to city `n - 1` after processing the **first** `i + 1` queries.

<https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-ii/>

**Example 1:**

> Input: `n = 5, queries = [[2,4],[0,2],[0,4]]`
> Output: `[3,2,1]`
> Explanation:
> {% invert %}
![case1-1](assets/3243-shortest-distance-after-road-addition-queries-i/case1-1.png)
{% endinvert %}
> After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.
> {% invert %}
![case1-2](assets/3243-shortest-distance-after-road-addition-queries-i/case1-2.png)
{% endinvert %}
> After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.
> {% invert %}
![case1-3](assets/3243-shortest-distance-after-road-addition-queries-i/case1-3.png)
{% endinvert %}
> After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

**Example 2:**

> Input: `n = 4, queries = [[0,3],[0,2]]`
> Output: `[1,1]`
> Explanation:
> {% invert %}
![case2-1](assets/3243-shortest-distance-after-road-addition-queries-i/case2-1.png)
{% endinvert %}
> After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.
> {% invert %}
![case2-2](assets/3243-shortest-distance-after-road-addition-queries-i/case2-2.png)
{% endinvert %}
> After the addition of the road from 0 to 2, the length of the shortest path remains 1.

**Constraints:**

- `3 <= n <= 10⁵`
- `1 <= queries.length <= 10⁵`
- `queries[i].length == 2`
- `0 <= queries[i][0] < queries[i][1] < n`
- `1 < queries[i][1] - queries[i][0]`
- There are no repeated roads among the queries.
- There are no two queries such that `i != j` and `queries[i][0] < queries[j][0] < queries[i][1] < queries[j][1]`.

## Test Cases

``` python
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
```

{% asset_code coding/assets/3244-shortest-distance-after-road-addition-queries-ii/solution_test.py %}

## Thoughts

这是 [3243. Shortest Distance After Road Addition Queries I](../3243-shortest-distance-after-road-addition-queries-i/index.md) 的进阶版，增加了限制条件，任意两条道路不会交叉。

因为道路不会交叉，设有一条道路 `[u, v]`，那么城市 `u` 和 `v` 之间的城市（即 `[u+1, u+2, ..., v-2, v-1]`）就都可以忽略掉（因为对于任何 `u < i < v`，从城市 `i` 出发，不可能一步走到 `v` 之后）。所有的道路都加好之后，剩下的城市就是从 `0` 走到 `n-1` 的必经点，剩余城市个数减去一就是距离。

记录从城市 i 出发，一步可以走到的最远的城市为 `f[i]`。初始时 `f[i] = i + 1`。

初始的时候，集合中有所有城市。增加一条道路 `[u, v]` 时，如果 `u` 已经不在集合中或者 `v <= f[u]`，则这条道路对于缩短距离没有帮助，直接忽略。否则就把集合中所有 `u < i < v` 的城市 `i` 都删掉。删的时候不需要遍历 `u` 到 `v` 的所有值，因为现在集合中只有 `f[u], f[f[u]], ..., f[...f[u]] < v`，依次删掉这些即可。

把 `f[u]` 从集合中删掉，并继续看 `f[f[u]]`，直到走到 `v` 就停止，然后将 `f[u]` 的值更新为 `v`。

附加的空间复杂度 `O(n)`。时间复杂度 `O(n + q)`，因为除了遍历所有 query 之外，相当于每个城市都加入再移出集合各一次。

写代码的时候不用真的创建一个包含所有城市的集合，再逐个去掉没用的。实际上当城市 i 从集合中删除后，`f[i]` 就没用了，可以给 `f[i]` 赋一个非法值（如 `n`）表示被删除了。而剩余城市的数量可以在每次去掉某个城市时直接减去一（循环逻辑保证不会多次去掉同一个城市）。

## Code

{% asset_code coding/assets/3244-shortest-distance-after-road-addition-queries-ii/solution.py %}
