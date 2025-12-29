---
title: 3151. Special Array I
notebook: coding
tags:
- easy
date: 2024-12-09 09:54:48
updated: 2024-12-09 09:54:48
---
## Problem

An array is considered **special** if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers `nums`. Return `true` if `nums` is a **special** array, otherwise, return `false`.

<https://leetcode.com/problems/special-array-i/>

**Example 1:**

> Input: `nums = [1]`
> Output: `true`
> Explanation:
> There is only one element. So the answer is true.

**Example 2:**

> Input: `nums = [2,1,4]`
> Output: `true`
> Explanation:
> There is only two pairs: `(2,1)` and `(1,4)`, and both of them contain numbers with different parity. So the answer is true.

**Example 3:**

> Input: `nums = [4,3,1,6]`
> Output: `false`
> Explanation:
> `nums[1]` and `nums[2]` are both odd. So the answer is false.

**Constraints:**

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Test Cases

```python
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
```

{% asset_code coding/3151-special-array-i/solution_test.py %}

## Thoughts

## Code

{% asset_code coding/3151-special-array-i/solution.py %}
