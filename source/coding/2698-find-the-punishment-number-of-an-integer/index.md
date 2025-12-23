---
title: 2698. Find the Punishment Number of an Integer
notebook: coding
tags:
- medium
date: 2025-02-15 16:18:38
updated: 2025-02-15 16:18:38
---
## Problem

Given a positive integer `n`, return _the **punishment number**_ of `n`.

The **punishment number** of `n` is defined as the sum of the squares of all integers `i` such that:

- `1 <= i <= n`
- The decimal representation of `i * i` can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals `i`.
- > `i * i` 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 `i`。

<https://leetcode.com/problems/find-the-punishment-number-of-an-integer/>

**Example 1:**

> Input: `n = 10`
> Output: `182`
> Explanation: There are exactly 3 integers i in the range `[1, 10]` that satisfy the conditions in the statement:
>
> - 1 since `1 * 1 = 1`
> - 9 since `9 * 9 = 81` and 81 can be partitioned into 8 and 1 with a sum equal to `8 + 1 == 9`.
> - 10 since `10 * 10 = 100` and 100 can be partitioned into 10 and 0 with a sum equal to `10 + 0 == 10`.
>
> Hence, the punishment number of 10 is `1 + 81 + 100 = 182`

**Example 2:**

> Input: `n = 37`
> Output: `1478`
> Explanation: There are exactly 4 integers i in the range `[1, 37]` that satisfy the conditions in the statement:
>
> - 1 since `1 * 1 = 1`.
> - 9 since `9 * 9 = 81` and 81 can be partitioned into `8 + 1`.
> - 10 since `10 * 10 = 100` and 100 can be partitioned into `10 + 0`.
> - 36 since `36 * 36 = 1296` and 1296 can be partitioned into `1 + 29 + 6`.
>
> Hence, the punishment number of 37 is `1 + 81 + 100 + 1296 = 1478`

**Constraints:**

- `1 <= n <= 1000`

## Test Cases

``` python
class Solution:
    def punishmentNumber(self, n: int) -> int:
```

{% asset_code coding/assets/2698-find-the-punishment-number-of-an-integer/solution_test.py %}

## Thoughts

先找出 `[1, n]` 中所有符合条件的 i（即 `i * i` 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 `i`）。

对于指定的数字 i，判定是否符合上述条件。令 `s = str(i * i)`，用回溯穷举所有可能的组合，看是否存在一个组合，各部分数字之和等于 i。

对于 s，设起长度为 m，则依次取前 k 个数字（`1 ≤ k ≤ m`），递归地判定剩下的字符串（`s[k:]`）是否能够组合出 `i - int(s[:k])`。

这些可以放到预处理中，设 n 的上限为 N（题中 `N = 1000`）。对于数字 i，判断是否符合条件的时间复杂度大约为 `O(2ᵐ) = O(i)`（其中 `m = O(log i)`）。所以判断 `[1, N]` 所有数字是否符合条件的时间复杂度为 `O(N²)`。

用有序数组记录所有符合条件的数字，可以再用同样大小的数组，记录所有前缀子数组的平方和。这样对于指定的 n，可以用二分法快速查找到小于等于 n 的最大的符合条件的数字，然后直接利用第二个数组得到对应的 punishment number。

预处理的时间复杂度为 `O(N²)`。`punishmentNumber` 方法的时间复杂度为 `O(log n)`。

## Code

{% asset_code coding/assets/2698-find-the-punishment-number-of-an-integer/solution.py %}
