---
title: 825. Friends Of Appropriate Ages
notebook: coding
tags:
- medium
date: 2024-11-17 09:50:39
updated: 2024-11-17 09:50:39
---
## Problem

There are `n` persons on a social media website. You are given an integer array `ages` where `ages[i]` is the age of the `iᵗʰ` person.

A Person `x` will not send a friend request to a person `y` (`x != y`) if any of the following conditions is true:

- `age[y] <= 0.5 * age[x] + 7`
- `age[y] > age[x]`
- `age[y] > 100 && age[x] < 100`

Otherwise, `x` will send a friend request to `y`.

Note that if `x` sends a request to `y`, `y` will not necessarily send a request to `x`. Also, a person will not send a friend request to himself.

Return _the total number of friend requests made_.

<https://leetcode.cn/problems/friends-of-appropriate-ages/>

**Example 1:**

> Input: `ages = [16,16]`
> Output: `2`
> Explanation: 2 people friend request each other.

**Example 2:**

> Input: `ages = [16,17,18]`
> Output: `2`
> Explanation: Friend requests are made 17 -> 16, 18 -> 17.

**Example 3:**

> Input: `ages = [20,30,100,110,120]`
> Output: `3`
> Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

**Constraints:**

- `n == ages.length`
- `1 <= n <= 2 * 10⁴`
- `1 <= ages[i] <= 120`

## Test Cases

```python
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

第三个条件似乎没用？当 `age[y] > 100 && age[x] < 100` 成立的时候，第二条的 `age[y] > age[x]` 一定成立。

::: invert-when-dark
{% diagramsnet condition.drawio %}
:::

条件一对应图中斜线下方的梯形区域，条件二对应对角线上方的三角形区域，条件三是条件二区域内部靠上部分的那个长条矩形。

排除掉三个条件的限制，图中网格填充的三角形区域是会发送邀请的 `age[y]` 和 `age[x]` 的关系，即 `0.5 * age[x] + 7 < age[y] <= age[x]`。

因为年龄数值是 1 到 120 之间的整数，用桶排序，统计每个年龄的人数，并算出小于等于每个年龄的总人数。

对于任何一个年龄，计算这个年龄的人会给哪个年龄范围的人发邀请，算出这个年龄区间的总人数。

空间复杂度 `O(1)`，时间复杂度 `O(n)`。

## Code

{% snippet solution.py %}
