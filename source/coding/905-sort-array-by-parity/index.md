---
title: 905. Sort Array By Parity
notebook: coding
tags:
- easy
date: 2025-02-04 14:17:44
updated: 2025-02-04 14:17:44
---
## Problem

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return _**any array** that satisfies this condition_.

<https://leetcode.cn/problems/sort-array-by-parity/>

**Example 1:**

> Input: `nums = [3,1,2,4]`
> Output: `[2,4,3,1]`
> Explanation: The outputs `[4,2,3,1]`, `[2,4,1,3]`, and `[4,2,1,3]` would also be accepted.

**Example 2:**

> Input: `nums = [0]`
> Output: `[0]`

**Constraints:**

- `1 <= nums.length <= 5000`
- `0 <= nums[i] <= 5000`

## Test Cases

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
```

{% asset_code solution_test.py %}

## Thoughts

用两个指针分别从数组首尾向中间扫描，即 `i = 0` 和 `j = n - 1`。如果 `nums[i]` 是偶数则右移 i 直到遇到奇数（或与 j 相遇），如果 `nums[j]` 是奇数则左移 j 直到遇到偶数（或与 i 相遇）。停下时如果 i 和 j 未相遇，说明 `nums[i]` 是奇数而 `nums[j]` 是偶数，将二者交换。重复处理直到 i 和 j 相遇即可。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code solution.py %}
