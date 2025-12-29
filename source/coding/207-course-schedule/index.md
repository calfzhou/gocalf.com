---
title: 207. Course Schedule
notebook: coding
tags:
- medium
date: 2024-11-22 17:17:02
updated: 2024-11-22 17:17:02
---
## Problem

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [aᵢ, bᵢ]` indicates that you **must** take course `bᵢ` first if you want to take course `aᵢ`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

<https://leetcode.com/problems/course-schedule/>

**Example 1:**

> Input: `numCourses = 2, prerequisites = [[1,0]]`
> Output: `true`
> Explanation: There are a total of 2 courses to take.
> To take course 1 you should have finished course 0. So it is possible.

**Example 2:**

> Input: `numCourses = 2, prerequisites = [[1,0],[0,1]]`
> Output: `false`
> Explanation: There are a total of 2 courses to take.
> To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

**Constraints:**

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= aᵢ, bᵢ < numCourses`
- All the pairs `prerequisites[i]` are **unique**.

## Test Cases

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
```

{% asset_code coding/207-course-schedule/solution_test.py %}

## Thoughts

所有课程作为节点，在有依赖关系的课程节点间加有向边，判定图中是否存在环，有环则返回 `false`，否则返回 `true`。

任取一个节点，从它出发做深度遍历，如果当前路径上的节点被再次访问到，说明有环。关键是要能够标记并识别到当前路径上的节点，以及从一个任选节点遍历完成后，如何选取下一个节点开始遍历。

先标记所有节点为「未处理」。任选一个「未处理」的节点，标记为「处理中」，递归遍历其下游节点，完成后将该节点标记为「已处理」。遍历下游节点时，如果是「已处理」可以忽略，如果是「未处理」则标记为「处理中」并递归，如果是「处理中」则说明遇到了当前路径上的节点，证明有环。

关键点就是节点的「处理中」状态。

另外如果用栈模拟递归的话，需要在遍历下游节点前标记为「处理中」，还要在遍历完之后修改标记为「以处理」。这就要确保所有下游节点出栈之后，当前节点才出栈。

因为输入是节点数和所有的边，要先把图构建出来。用邻接表法，对每个节点，记录以其为起点的边的终点。

## Code

{% asset_code coding/207-course-schedule/solution.py %}
