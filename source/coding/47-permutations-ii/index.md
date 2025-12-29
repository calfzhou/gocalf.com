---
title: 47. Permutations II
notebook: coding
tags:
- easy
date: 2025-02-06 15:49:38
updated: 2025-02-06 15:49:38
---
## Problem

Given a collection of numbers, `nums`, that might contain duplicates, return _all possible unique permutations **in any order**._

<https://leetcode.cn/problems/permutations-ii/>

**Example 1:**

> Input: `nums = [1,1,2]`
> Output:
>
> ```json
> [[1,1,2],
> [1,2,1],
> [2,1,1]]
> ```

**Example 2:**

> Input: `nums = [1,2,3]`
> Output: `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

**Constraints:**

- `1 <= nums.length <= 8`
- `-10 <= nums[i] <= 10`

## Test Cases

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
```

{% asset_code coding/47-permutations-ii/solution_test.py %}

## Thoughts

[46. Permutations](../46-permutations/index.md) 的进阶版，可以有重复元素，但结果排列要去重。

首先对 nums 排序，这样相同的数字会相邻在一起。然后先照搬 [problem 46](../46-permutations/index.md) 的代码，在对重复数字做处理。

在 [problem 46](../46-permutations/index.md) 中用集合记录待排列的数字，但本题中因为有重复就不能用了。可以改成字典（key 为数字，值为词频），或者就要有序的数组。给当前位置选数字的时候，从各不相同的数字中选取（即相同的多个数字只选一次）即可。

时间和空间复杂度是类似的。

## Code

{% asset_code coding/47-permutations-ii/solution.py %}
