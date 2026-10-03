---
title: 1705. Maximum Number of Eaten Apples
notebook: coding
tags:
- medium
date: 2024-12-24 10:12:56
updated: 2024-12-24 10:12:56
---
## Problem

There is a special kind of apple tree that grows apples every day for `n` days. On the `iᵗʰ` day, the tree grows `apples[i]` apples that will rot after `days[i]` days, that is on day `i + days[i]` the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by `apples[i] == 0` and `days[i] == 0`.

You decided to eat **at most** one apple a day (to keep the doctors away). Note that you can keep eating after the first `n` days.

Given two integer arrays `days` and `apples` of length `n`, return _the maximum number of apples you can eat._

<https://leetcode.cn/problems/maximum-number-of-eaten-apples/>

**Example 1:**

> Input: `apples = [1,2,3,5,2], days = [3,2,1,4,2]`
> Output: `7`
> Explanation: You can eat 7 apples:
>
> - On the first day, you eat an apple that grew on the first day.
> - On the second day, you eat an apple that grew on the second day.
> - On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
> - On the fourth to the seventh days, you eat apples that grew on the fourth day.

**Example 2:**

> Input: `apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]`
> Output: `5`
> Explanation: You can eat 5 apples:
>
> - On the first to the third day you eat apples that grew on the first day.
> - Do nothing on the fouth and fifth days.
> - On the sixth and seventh days you eat apples that grew on the sixth day.

**Constraints:**

- `n == apples.length == days.length`
- `1 <= n <= 2 * 10⁴`
- `0 <= apples[i], days[i] <= 2 * 10⁴`
- `days[i] = 0` if and only if `apples[i] = 0`.

## Test Cases

```python
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

显然每天都应该吃最快要过期的苹果（先吃快烂了的苹果，还是先吃最新鲜的苹果，似乎是两种不同的生活态度）。

利用最小堆做成优先队列，每天收获的新苹果，计算出保质期是到哪天，放入堆中。堆顶是过期时间最早的苹果。

每天检查堆顶的苹果是否已经到期或过期，是就丢弃。否则就吃掉一个堆顶的苹果。如果这一拨苹果吃光了，则弹出。

n 天之后，不会再有新的苹果，可以一次计算出堆顶的一拨苹果最多能吃几天，不用真的一天一天地累加。

## Code

{% snippet solution.py %}
