---
title: 541. Reverse String II
notebook: coding
tags:
- easy
date: 2025-01-31 21:56:25
updated: 2025-01-31 21:56:25
---
## Problem

Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k` characters counting from the start of the string.

If there are fewer than `k` characters left, reverse all of them. If there are less than `2k` but greater than or equal to `k` characters, then reverse the first `k` characters and leave the other as original.

<https://leetcode.cn/problems/reverse-string-ii/>

**Example 1:**

> Input: `s = "abcdefg", k = 2`
> Output: `"bacdfeg"`

**Example 2:**

> Input: `s = "abcd", k = 2`
> Output: `"bacd"`

**Constraints:**

- `1 <= s.length <= 10⁴`
- `s` consists of only lowercase English letters.
- `1 <= k <= 10⁴`

## Test Cases

``` python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
```

{% asset_code coding/assets/541-reverse-string-ii/solution_test.py %}

## Thoughts

[344. Reverse String](../344-reverse-string/index.md) 的进阶版，每 k 个字符为一段，对间隔的段做翻转。

先把 s 的所有字符放在数组里，然后分别对 `s[0:k]`、`s[2k:3k]`、`s[4k:5k]`、……按照 [344. Reverse String](../344-reverse-string/index.md) 的逻辑进行翻转即可。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/assets/541-reverse-string-ii/solution.py %}
