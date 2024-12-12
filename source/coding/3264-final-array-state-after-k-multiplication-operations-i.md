---
title: 3264. Final Array State After K Multiplication Operations I
notebook: coding
tags:
- easy
date: 2024-12-13 01:36:18
updated: 2024-12-13 01:36:18
---
## Problem

You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

You need to perform `k` operations on `nums`. In each operation:

- Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the minimum value, select the one that appears **first**.
- Replace the selected minimum value `x` with `x * multiplier`.

Return an integer array denoting the _final state_ of `nums` after performing all `k` operations.

<https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-i/>

**Example 1:**

> Input: `nums = [2,1,3,5,6], k = 5, multiplier = 2`
> Output: `[8,4,6,5,6]`
> Explanation:
>
> | Operation         | Result            |
> |-------------------|-------------------|
> | After operation 1 | `[2, 2, 3, 5, 6]` |
> | After operation 2 | `[4, 2, 3, 5, 6]` |
> | After operation 3 | `[4, 4, 3, 5, 6]` |
> | After operation 4 | `[4, 4, 6, 5, 6]` |
> | After operation 5 | `[8, 4, 6, 5, 6]` |

**Example 2:**

> Input: `nums = [1,2], k = 3, multiplier = 4`
> Output: `[16,8]`
> Explanation:
>
> | Operation         | Result    |
> |-------------------|-----------|
> | After operation 1 | `[4, 2]`  |
> | After operation 2 | `[4, 8]`  |
> | After operation 3 | `[16, 8]` |

**Constraints:**

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= k <= 10`
- `1 <= multiplier <= 5`

## Test Cases

``` python
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
```

{% asset_code coding/3264-final-array-state-after-k-multiplication-operations-i/solution_test.py %}

## Thoughts

跟 [2558. Take Gifts From the Richest Pile](2558-take-gifts-from-the-richest-pile) 几乎一模一样，最大的区别就是这道题在有遇到重复数字的时候需要保持原有顺序，而且最后还要按原始顺序返回结果数组。那就也是用最小堆，但把数组下标和元素数值一起作为堆中的元素，这样当数值相等时，可以让数组下标小的排在前边。最后也可以根据这些下边构建结果数组。

时间复杂度 `O(n + k log n)`，空间复杂度 `O(n)`。

当然这道题限定的 n 极小，那么跟 [2931. Maximum Spending After Buying Items](2931-maximum-spending-after-buying-items) 类似，用堆的常数系数过大导致实际运行速度并不一定快，直接在每次循环里遍历数组查找最小值也问题不大，时间复杂度 `O(k * n)`，空间复杂度 `O(1)`（直接在原数组上修改）。

## Code

## Min Heap

{% asset_code coding/3264-final-array-state-after-k-multiplication-operations-i/solution.py %}

## Find Directly

{% asset_code coding/3264-final-array-state-after-k-multiplication-operations-i/solution2.py %}
