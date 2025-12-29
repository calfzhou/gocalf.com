---
title: 1415. The k-th Lexicographical String of All Happy Strings of Length n
notebook: coding
tags:
- medium
date: 2025-02-19 11:07:53
updated: 2025-02-19 11:07:53
---
## Problem

A **happy string** is a string that:

- consists only of letters of the set `['a', 'b', 'c']`.
- `s[i] != s[i + 1]` for all values of `i` from `1` to `s.length - 1` (string is 1-indexed).

For example, strings **"abc", "ac", "b"** and **"abcbabcbcb"** are all happy strings and strings **"aa", "baa"** and **"ababbc"** are not happy strings.

Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted in lexicographical order.

Return _the kᵗʰ string_ of this list or return an **empty string** if there are less than `k` happy strings of length `n`.

<https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/>

**Example 1:**

> Input: `n = 1, k = 3`
> Output: `"c"`
> Explanation: The list `["a", "b", "c"]` contains all happy strings of length 1. The third string is `"c"`.

**Example 2:**

> Input: `n = 1, k = 4`
> Output: `""`
> Explanation: There are only 3 happy strings of length 1.

**Example 3:**

> Input: `n = 3, k = 9`
> Output: `"cab"`
> Explanation: There are 12 different happy string of length 3 `["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]`. You will find the 9ᵗʰ string = `"cab"`

**Constraints:**

- `1 <= n <= 10`
- `1 <= k <= 100`

## Test Cases

```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
```

{% asset_code coding/1415-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/solution_test.py %}

## Thoughts

Happy string 除了第一位有 `'a'`、`'b'`、`'c'` 三个选择外，之后的每一位都只有两个选择——即与前一位不同的两个字母。如果用 `0` 表示这两个字母中较小的那个，用 `1` 表示较大的那个，显然 happy string 除去第一位之外，剩下的 `n - 1` 位对应了一个二进制数，一共有 `2ⁿ⁻¹` 个可能。而第一位共有三个可能，所以长度为 n 的 happy string 最多有 `3 * 2ⁿ⁻¹` 个。

如果 `k > 3 * 2ⁿ⁻¹`，直接返回空字符串。

否则用 `k - 1` 除以 `2ⁿ⁻¹`，商必然在 0 到 2 之间，分别对应 `'a'`、`'b'`、`'c'`；余数转成 `n - 1` 位的二进制表达，从最高位开始，根据前边对 `0` 和 `1` 的定义，就可以逐位构造出 happy string。显然得到的 happy string 就是所有长度为 n 的 happy strings 中按字典序第 k 大的。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/1415-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/solution.py %}
