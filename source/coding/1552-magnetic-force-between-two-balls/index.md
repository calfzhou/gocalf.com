---
title: 1552. Magnetic Force Between Two Balls
notebook: coding
tags:
- medium
date: 2025-02-14 11:33:46
updated: 2025-02-14 11:33:46
---
## Problem

In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has `n` empty baskets, the `iᵗʰ` basket is at `position[i]`, Morty has `m` balls and needs to distribute the balls into the baskets such that the **minimum magnetic force** between any two balls is **maximum**.

Rick stated that magnetic force between two different balls at positions `x` and `y` is `|x - y|`.

Given the integer array `position` and the integer `m`. Return _the required force_.

<https://leetcode.cn/problems/magnetic-force-between-two-balls/>

**Example 1:**

{% invert %}
![case1](assets/1552-magnetic-force-between-two-balls/case1.png)
{% endinvert %}

> Input: `position = [1,2,3,4,7], m = 3`
> Output: `3`
> Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs `[3, 3, 6]`. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

**Example 2:**

> Input: `position = [5,4,3,2,1,1000000000], m = 2`
> Output: `999999999`
> Explanation: We can use baskets 1 and 1000000000.

**Constraints:**

- `n == position.length`
- `2 <= n <= 10⁵`
- `1 <= position[i] <= 10⁹`
- All integers in `position` are **distinct**.
- `2 <= m <= position.length`

## Test Cases

``` python
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
```

{% asset_code coding/1552-magnetic-force-between-two-balls/solution_test.py %}

## Thoughts

跟 [1760. Minimum Limit of Balls in a Bag](../1760-minimum-limit-of-balls-in-a-bag/index.md) 的 [二分法](../1760-minimum-limit-of-balls-in-a-bag/index.md#二分法) 思路差不多。因为 position 的值是离散的，想直接计算出结果比较困难，但可以快速验证给定的一个最小磁力是否能够达成。

对于给定的一个最小磁力值 force，如果能够摆得出来，那么更小的 force 也一定能摆得出来；如果摆不出来，那么更大的 force 也一定摆不出来。由此可以使用二分法找到分界点。

显然下界为 1。如果 position 中任意需要的位置都存在，那么上界为 `(max{position} - min{position}) // (m - 1)`（即最均匀地摆放）。

对于给定的 force，用贪心的办法从最左侧开始依次摆放每个球，看是否能把 m 个球全都摆好，时间复杂度 `O(n)`（需要事先对 position 排序）。

总的时间复杂度为 `O(n * (log n + log p - log m))`，其中 p 是 position 的最大值。额外的空间复杂度 `O(1)`。

## Code

{% asset_code coding/1552-magnetic-force-between-two-balls/solution.py %}
