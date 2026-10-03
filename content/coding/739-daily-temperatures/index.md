---
title: 739. Daily Temperatures
notebook: coding
tags:
- medium
date: 2024-12-18 17:20:13
updated: 2024-12-18 23:33:05
---
## Problem

Given an array of integers `temperatures` represents the daily temperatures, return _an array_ `answer` _such that_ `answer[i]` _is the number of days you have to wait after the_ `iᵗʰ` _day to get a warmer temperature_. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

<https://leetcode.com/problems/daily-temperatures/>

**Example 1:**

> Input: `temperatures = [73,74,75,71,69,72,76,73]`
> Output: `[1,1,4,2,1,1,0,0]`

**Example 2:**

> Input: `temperatures = [30,40,50,60]`
> Output: `[1,1,1,0]`

**Example 3:**

> Input: `temperatures = [30,60,90]`
> Output: `[1,1,0]`

**Constraints:**

- `1 <= temperatures.length <= 10⁵`
- `30 <= temperatures[i] <= 100`

## Test Cases

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
```

{% snippet solution_test.py %}

## Thoughts

跟 [496. Next Greater Element I](../496-next-greater-element-i/index.md) 和 [503. Next Greater Element II](../503-next-greater-element-ii/index.md) 类似，本质都是求当前元素右侧第一个比当前元素大的数，利用单调栈求解。本题是要计算找到的 next greater 温度的下标，与当前温度下标的差值。为了方便得到 next greater 的下标，直接把下标入栈。

## Code

### Backward Iteration

{% snippet solution.py %}

### Forward Iteration

{% snippet solution2.py %}

这里用正向循环就可以做 in-place 修改。
