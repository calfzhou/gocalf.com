---
title: 1980. Find Unique Binary String
notebook: coding
tags:
- medium
date: 2025-02-20 09:57:26
updated: 2025-02-20 09:57:26
---
## Problem

Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return _a binary string of length_ `n` _that **does not appear** in_ `nums`_. If there are multiple answers, you may return **any** of them_.

<https://leetcode.com/problems/find-unique-binary-string/>

**Example 1:**

> Input: `nums = ["01","10"]`
> Output: `"11"`
> Explanation: `"11"` does not appear in nums. `"00"` would also be correct.

**Example 2:**

> Input: `nums = ["00","01"]`
> Output: `"11"`
> Explanation: `"11"` does not appear in nums. `"10"` would also be correct.

**Example 3:**

> Input: `nums = ["111","011","001"]`
> Output: `"101"`
> Explanation: `"101"` does not appear in nums. `"000"`, `"010"`, `"100"`, and `"110"` would also be correct.

**Constraints:**

- `n == nums.length`
- `1 <= n <= 16`
- `nums[i].length == n`
- `nums[i]` is either `'0'` or `'1'`.
- All the strings of `nums` are **unique**.

## Test Cases

```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
```

{% snippet solution_test.py %}

## Thoughts

取 0 到 n（包含）的所有整数（共 `n + 1` 个），这些数字都可以表达成长度为 n 的二进制形式（左补零），且根据鸽笼原理，这 `n + 1` 个整数中，至少有一个不在 `nums` 中。

用一个集合记录 `[0, n]` 区间内所有整数，遍历 nums，对于 nums 中的每一个二进制串，转成整数后从集合中删除该数字。最后集合中至少会剩余一个数字。从集合剩余的数字中任取一个，格式化为长度为 n 的二进制字符串，返回即可。

时间复杂度 `O(n²)`，空间复杂度 `O(n)`。

## Code

{% snippet solution.py %}
