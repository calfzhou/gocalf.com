---
title: 1847. Closest Room
notebook: coding
tags:
- hard
date: 2024-12-16 23:50:39
updated: 2024-12-26 00:04:19
---
## Problem

There is a hotel with `n` rooms. The rooms are represented by a 2D integer array `rooms` where `rooms[i] = [roomIdᵢ, sizeᵢ]` denotes that there is a room with room number `roomIdᵢ` and size equal to `sizeᵢ`. Each `roomIdᵢ` is guaranteed to be **unique**.

You are also given `k` queries in a 2D array `queries` where `queries[j] = [preferredⱼ, minSizeⱼ]`. The answer to the `jᵗʰ` query is the room number `id` of a room such that:

- The room has a size of **at least** `minSizeⱼ`, and
- `abs(id - preferredⱼ)` is **minimized**, where `abs(x)` is the absolute value of `x`.

If there is a **tie** in the absolute difference, then use the room with the **smallest** such `id`. If there is **no such room**, the answer is `-1`.

Return _an array_ `answer` _of length_ `k` _where_ `answer[j]` _contains the answer to the_ `jᵗʰ` _query_.

<https://leetcode.cn/problems/closest-room/>

**Example 1:**

> Input: `rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]`
> Output: `[3,-1,3]`
> Explanation: The answers to the queries are as follows:
> Query = `[3,1]`: Room number 3 is the closest as `abs(3 - 3) = 0`, and its size of 2 is at least 1. The answer is 3.
> Query = `[3,3]`: There are no rooms with a size of at least 3, so the answer is -1.
> Query = `[5,2]`: Room number 3 is the closest as `abs(3 - 5) = 2`, and its size of 2 is at least 2. The answer is 3.

**Example 2:**

> Input: `rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]`
> Output: `[2,1,3]`
> Explanation: The answers to the queries are as follows:
> Query = `[2,3]`: Room number 2 is the closest as `abs(2 - 2) = 0`, and its size of 3 is at least 3. The answer is 2.
> Query = `[2,4]`: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
> Query = `[2,5]`: Room number 3 is the only room with a size of at least 5. The answer is 3.

**Constraints:**

- `n == rooms.length`
- `1 <= n <= 10⁵`
- `k == queries.length`
- `1 <= k <= 10⁴`
- `1 <= roomIdᵢ, preferredⱼ <= 10⁷`
- `1 <= sizeᵢ, minSizeⱼ <= 10⁷`

## Test Cases

``` python
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
```

{% asset_code coding/assets/1847-closest-room/solution_test.py %}

## Thoughts

对于一个 query，可以把所有 `size >= minSize` 的房间找出来，在这些房间中找距离 `preferred` 最近的编号。如果这些房间是按照编号排序的，就可以用二分查找。

如果下一个 query 的 `minSize` 更小一些，那么可以往这个房间集合中再加入那些 `size` 不小于新 query 的 `minSize` 的房间，如果还能保持按编号排序，就还可以用二分查找。

所以对 `queries` 按 `minSize` 降序排列，这样每下一个 query 的 `minSize` 都不会比前一个大。对 `rooms` 也按 `size` 降序排列，用两个下标分别跟踪 `queries` 和 `rooms`，可以方便地对每个新 query 找出增量的房间。

关键在于用一个「能保持有序」的容器保存按 `minSize` 筛出来的房间，在不断加入新房间的同时保持按房间编号排序。

暂不考虑 [grantjenks/python-sortedcontainers: Python Sorted Container Types: Sorted List, Sorted Dict, and Sorted Set](https://github.com/grantjenks/python-sortedcontainers) 之类的第三方工具，很容易想到的是二叉查找树（Binary Search Tree），或其变体如 AVL 树（Georgy **A**delson-**V**elsky and Evgenii **L**andis Tree）、红黑树（Red Black Tree）等。

> 先试了一下 BST，果然很慢（因为非常不平衡）。只好修改插入的方法，使其成为 AVL 树，快了十倍。本题不涉及删除节点，不用红黑树也可以。

AVL 树的详细信息参见 [DSA AVL Trees](https://www.w3schools.com/dsa/dsa_data_avltrees.php)。

稍微修改一下树的查找方法，如果目标数字找不到，就返回小于目标数的最大值、以及大于目标树的最小值，这对于 BST 或其变体都很简单。

时间复杂度是 `O(n log n + k log k + k log n)`，其中 `O(n log n)` 是排序 `rooms` 和不断构建可选房间的有序集合的时间；`O(k log k)` 是排序 `queries` 的时间；`O(k log n)` 是对所有 queries，借助 BST 查找等于或最接近 query 中 `preferred` 房间编号的时间。

空间复杂度是 `O(n + k)`，其中 `O(n)` 是可选房间有序集合的空间（`rooms` 可以 in-place 排序）；`O(k)` 是对 `queries` 排序但需要保留原始下标所需的空间。

提交后的速度不是很快，也就 `7+%`。可能是 AVL 树的常数系数太大了吧。实际上对于 Python 而言，直接用数组（list）配合标准库里的 [bisect — Array bisection algorithm](https://docs.python.org/3/library/bisect.html) 就可以做到速度非常快（[sortedcontainers](https://github.com/grantjenks/python-sortedcontainers) 底层也是利用 list 和 bisect 库来实现的）。在本题限定的量级内，直接用 list 就已经足够快了（`100%`）（虽然插入的复杂度是 `O(n)`）。

## Code

### AVL Tree

> Runtime beats `7+%`:

{% asset_code coding/assets/1847-closest-room/solution.py %}

### Python list - Fast

> Runtime beats `100%`:

{% asset_code coding/assets/1847-closest-room/solution_fast.py %}

## Monotonic Stack

在 [2940. Find Building Where Alice and Bob Can Meet](../2940-find-building-where-alice-and-bob-can-meet/index.md) 中尝试 [基于单调栈 + 二分搜索的解法](../2940-find-building-where-alice-and-bob-can-meet/index.md#Monotonic-Stack) 时，觉得这道题也可以用类似的逻辑处理。

核心区别只有两个。一个是本题需要往两个方向找，既要找 preferred 右边第一个，也要找 preferred 左边第一个，可以通过两次循环达成。另一个是 preferred 不一定是存在的房间号，不能用跟 [problem 2940](../2940-find-building-where-alice-and-bob-can-meet/index.md#Monotonic-Stack) 一样的方式（即用当前扫描到的房间号查出 prefer 此房间号的所有查询），需要对 preferred 和 roomId 做分段匹配。

各种边界条件细节需要小心处理。

时间复杂度是 `O(n log n + k log k + k log n)`，空间复杂度 `O(n + k)`，跟上边一样。实际运行时间跟 [problem 2940](../2940-find-building-where-alice-and-bob-can-meet/index.md) 也很像，用单调栈比用有序集合慢一倍。

{% asset_code coding/assets/1847-closest-room/solution3.py %}
