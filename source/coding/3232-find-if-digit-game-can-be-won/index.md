---
title: 3232. Find if Digit Game Can Be Won
notebook: coding
tags:
- easy
date: 2024-11-30 09:36:15
updated: 2024-11-30 09:36:15
---
## Problem

You are given an array of **positive** integers `nums`.

Alice and Bob are playing a game. In the game, Alice can choose **either** all single-digit numbers or all double-digit numbers from `nums`, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is **strictly greater** than the sum of Bob's numbers.

Return `true` if Alice can win this game, otherwise, return `false`.

<https://leetcode.cn/problems/find-if-digit-game-can-be-won/>

**Example 1:**

> Input: `nums = [1,2,3,4,10]`
> Output: `false`
> Explanation:
> Alice cannot win by choosing either single-digit or double-digit numbers.

**Example 2:**

> Input: `nums = [1,2,3,4,5,14]`
> Output: `true`
> Explanation:
> Alice can win by choosing single-digit numbers which have a sum equal to 15.

**Example 3:**

> Input: `nums = [5,5,5,25]`
> Output: `true`
> Explanation:
> Alice can win by choosing double-digit numbers which have a sum equal to 25.

**Constraints:**

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 99`

## Test Cases

``` python
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
```

{% asset_code coding/assets/3232-find-if-digit-game-can-be-won/solution_test.py %}

## Thoughts

相当于判断所有一位数之和与所有两位数之和是否不相等。

## Code

{% asset_code coding/assets/3232-find-if-digit-game-can-be-won/solution.py %}
