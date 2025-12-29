---
title: 730. Count Different Palindromic Subsequences
notebook: coding
tags:
- hard
katex: true
date: 2024-12-31 21:29:10
updated: 2024-12-31 21:29:10
---
## Problem

Given a string s, return _the number of different non-empty palindromic subsequences in_ `s`. Since the answer may be very large, return it **modulo** `10⁹ + 7`.

A subsequence of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences `a₁, a₂, ...` and `b₁, b₂, ...` are different if there is some `i` for which `aᵢ != bᵢ`.

<https://leetcode.com/problems/count-different-palindromic-subsequences/>

**Example 1:**

> Input: `s = "bccb"`
> Output: `6`
> Explanation: The 6 different non-empty palindromic subsequences are `'b'`, `'c'`, `'bb'`, `'cc'`, `'bcb'`, `'bccb'`.
> Note that `'bcb'` is counted only once, even though it occurs twice.

**Example 2:**

> Input: `s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"`
> Output: `104860361`
> Explanation: There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo `10⁹ + 7`.

**Constraints:**

- `1 <= s.length <= 1000`
- `s[i]` is either `'a'`, `'b'`, `'c'`, or `'d'`.

## Test Cases

```python
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
```

{% asset_code coding/730-count-different-palindromic-subsequences/solution_test.py %}

## Thoughts

看起来是 [647. Palindromic Substrings](../647-palindromic-substrings/index.md) 的进阶版，从 **substring** 升级为 **subsequence**，而且要去重，不过字符种类从所有英文小写字母缩减到只有 `'a'`、`'b'`、`'c'` 和 `'d'` 四个。

考虑任意一个子区间 `[i, j]`（`0 ≤ i ≤ j < n`），定义 `dp(i, j)` 表示子字符串 `s[i:j+1]` 内各不相同的回文子序列总数。

关键在于如何避免重复。技巧是确定首（及尾）字母，首字母不同的一定是不同的回文。

不妨以 "a" 为例。先看 `s[i:j+1]` 内是否有 "a"，没有则跳过。如果有，那么单个字母 "a" 就是回文，计数加一。如果不止一个，那么 "aa" 也是回文，计数再加一。然后找到最左边和最右边的 "a"，设下标分别为 first 和 last（`i ≤ first < last ≤ j`），给 `s[first+1:last]` 中所有各不相同回文两头各加一个 "a"，仍然都是各不相同的回文。

可见 `s[i:j+1]` 中 **以 "a" 开头** 的回文总数为：

$$
\begin{cases}
  0 & \text{for }`a\text{\textquoteright}\notin s[i:j+1] \\
  1 & \text{for }\exists!`a\text{\textquoteright}\in s[i:j+1] \\
  dp(first+1,last-1)+2
\end{cases}
$$

> 第三个式子的 `+ 2`，一个代表 "a"，一个代表 "aa"。

同理可以得到 `s[i:j+1]` 中分别以 "b"、"c"、"d" 开头的回文总数，累加即可。

易知这样可以找出来所有各不相同的回文，既不会有重复，也不会遗漏。

自顶向下计算的话，可以用带缓存的递归。另外可以事先扫描 s，对于每个位置 i，记录四个字母在 `s[i:]` 最左边分别的位置，以及在 `s[:i+1]` 最右边分别的位置，以便对于指定的区间 `[i, j]`，可以用常数时间得到某个字母的 first 和 last。

整体时间复杂度为 `O(C * n²)`，空间复杂度 `O(n²)`。其中 C 是 s 中可能出现的各不相同的字符总数，本题中为 4 可以认为是常数。

## Code

{% asset_code coding/730-count-different-palindromic-subsequences/solution.py %}
