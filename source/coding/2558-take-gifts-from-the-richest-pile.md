---
title: 2558. Take Gifts From the Richest Pile
notebook: coding
tags:
- easy
date: 2024-12-12 11:26:06
updated: 2024-12-12 11:26:06
---
## Problem

You are given an integer array `gifts` denoting the number of gifts in various piles. Every second, you do the following:

- Choose the pile with the maximum number of gifts.
- If there is more than one pile with the maximum number of gifts, choose any.
- Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.

Return _the number of gifts remaining after_ `k` _seconds._

<https://leetcode.com/problems/take-gifts-from-the-richest-pile/>

**Example 1:**

> Input: `gifts = [25,64,9,4,100], k = 4`
> Output: `29`
> Explanation:
> The gifts are taken in the following way:
>
> - In the first second, the last pile is chosen and 10 gifts are left behind.
> - Then the second pile is chosen and 8 gifts are left behind.
> - After that the first pile is chosen and 5 gifts are left behind.
> - Finally, the last pile is chosen again and 3 gifts are left behind.
>
> The final remaining gifts are `[5,8,9,4,3]`, so the total number of gifts remaining is 29.

**Example 2:**

> Input: `gifts = [1,1,1,1], k = 4`
> Output: `4`
> Explanation:
> In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile.
> That is, you can't take any pile with you.
> So, the total gifts remaining are 4.

**Constraints:**

- `1 <= gifts.length <= 10³`
- `1 <= gifts[i] <= 10⁹`
- `1 <= k <= 10³`

## Test Cases

``` python
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
```

{% asset_code coding/2558-take-gifts-from-the-richest-pile/solution_test.py %}

## Thoughts

这种每次取走最大值，再放回另外一个值，重复操作的逻辑，最适合用堆来做。

> 这题比 [2931. Maximum Spending After Buying Items](2931-maximum-spending-after-buying-items) 更适合用堆。题目的难度等级设定比较迷。

Python 内置的 [heapq](https://docs.python.org/3/library/heapq.html) 实现的是最小堆，所以给 `gifts` 里所有的值加上负号来模拟最大堆。

时间复杂度 `O(k log n)`，空间复杂度 `O(n)`（构建单独的堆空间）或 `O(1)` 直接利用 `gifts` 原有空间。

## Code

{% asset_code coding/2558-take-gifts-from-the-richest-pile/solution.py %}
