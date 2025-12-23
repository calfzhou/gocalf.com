---
title: 2466. Count Ways To Build Good Strings
notebook: coding
tags:
- medium
date: 2024-12-30 10:19:17
updated: 2024-12-30 10:19:17
---
## Problem

Given the integers `zero`, `one`, `low`, and `high`, we can construct a string by starting with an empty string, and then at each step perform either of the following:

- Append the character `'0'` `zero` times.
- Append the character `'1'` `one` times.

This can be performed any number of times.

A **good** string is a string constructed by the above process having a **length** between `low` and `high` (**inclusive**).

Return _the number of **different** good strings that can be constructed satisfying these properties._ Since the answer can be large, return it **modulo** `10⁹ + 7`.

<https://leetcode.com/problems/count-ways-to-build-good-strings/>

**Example 1:**

> Input: `low = 3, high = 3, zero = 1, one = 1`
> Output: `8`
> Explanation:
> One possible valid good string is `"011"`.
> It can be constructed as follows: `"" -> "0" -> "01" -> "011"`.
> All binary strings from `"000"` to `"111"` are good strings in this example.

**Example 2:**

> Input: `low = 2, high = 3, zero = 1, one = 2`
> Output: `5`
> Explanation: The good strings are `"00"`, `"11"`, `"000"`, `"110"`, and `"011"`.

**Constraints:**

- `1 <= low <= high <= 10⁵`
- `1 <= zero, one <= low`

## Test Cases

``` python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
```

{% asset_code coding/2466-count-ways-to-build-good-strings/solution_test.py %}

## Thoughts

相当于 [70. Climbing Stairs](../70-climbing-stairs/index.md) 的进阶版，从固定的「1 步」和「2 步」升级为任意的「`zero` 个 `"0"`」和「`one` 个 `"1"`」。

所以定义 `dp(i)` 表示长度为 i 的不同 good 字符串的个数，则 `dp(i) = dp(i - zero) + dp(i - one)`。初值 `dp(0) = 1`。

最后把 `dp[low:high+1]` 累加即可。

因为只需要用到最近的 `zero` 或 `one` 个 dp 值，可以用队列保存最新的 `max{zero, one}` 个 dp 值，节省一点儿空间。

时间复杂度 `O(high)`，空间复杂度 `O(max{zero, one})`。

## Code

{% asset_code coding/2466-count-ways-to-build-good-strings/solution.py %}
