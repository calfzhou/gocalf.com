---
title: 664. Strange Printer
notebook: coding
tags:
- hard
katex: true
date: 2024-12-22 01:13:24
updated: 2024-12-22 01:13:24
---
## Problem

There is a strange printer with the following two special properties:

- The printer can only print a sequence of **the same character** each time.
- At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

Given a string `s`, return _the minimum number of turns the printer needed to print it_.

<https://leetcode.com/problems/strange-printer/>

**Example 1:**

> Input: s = "aaabbb"
> Output: 2
> Explanation: Print "aaa" first and then print "bbb".

**Example 2:**

> Input: s = "aba"
> Output: 2
> Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

**Constraints:**

- `1 <= s.length <= 100`
- `s` consists of lowercase English letters.

## Test Cases

``` python
class Solution:
    def strangePrinter(self, s: str) -> int:
```

{% asset_code coding/664-strange-printer/solution_test.py %}

## Thoughts

对于一个下标区间 `[i, j]`（`0 ≤ i ≤ j < n`），看如何打印对应的子字符串 `s[i..j]`（为了方便，用 `s[i..j]` 表示 `s[i:j+1]`）。

如果 `i = j`，显然需要打印一次 `s[i]`。下边看 `i < j` 的情况。

最简单办法就是先打印 `s[i]`，然后打印剩余的部分即 `s[i+1..j]`。

如果 `s[j] = s[i]`，那么跟打印 `s[i..j-1]` 没区别。

如果区间内还有一个下标 k，`i < k < j`，`s[k] = s[i]`，那么可以先打印 `s[i..k]`，再打印 `s[k+1..j]`。而其中 `s[i..k]` 部分跟 `s[i..k-1]` 的打印次数是一样的。对所有可能的 k 进行枚举，而如果 `s[j] = s[i]`，可以把 j 也当作特殊的 k 去处理。

定义 `dp(i, j)` 表示打印 `s[i..j]` 所需的最少次数。

$$
\begin{cases}
  dp(j,i)=0 \\
  dp(i,i)=1 \\
  dp(i,j)=\min_k\begin{cases}
    1+dp(i+1,j) \\
    dp(i,k-1)+dp(k+1,j) & \text{for }s[k]=s[i]
  \end{cases}
\end{cases}
$$

注意边界情况。

时间复杂度大约 `O(n³)`，空间复杂度 `O(n²)`。

## Code

### Iteratively

{% asset_code coding/664-strange-printer/solution.py %}

### Recursively

{% asset_code coding/664-strange-printer/solution2.py %}
