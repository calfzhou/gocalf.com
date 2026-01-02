---
title: 2981. Find Longest Special Substring That Occurs Thrice I
notebook: coding
tags:
- medium
katex: true
date: 2024-12-10 16:36:27
updated: 2024-12-10 16:47:34
---
## Problem

You are given a string `s` that consists of lowercase English letters.

A string is called **special** if it is made up of only a single character. For example, the string `"abc"` is not special, whereas the strings `"ddd"`, `"zz"`, and `"f"` are special.

Return _the length of the **longest special substring** of_ `s` _which occurs **at least thrice**_, _or_ `-1` _if no special substring occurs at least thrice_.

A **substring** is a contiguous **non-empty** sequence of characters within a string.

<https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/>

**Example 1:**

> Input: `s = "aaaa"`
> Output: `2`
> Explanation: The longest special substring which occurs thrice is "aa": substrings "{% u aa %}aa", "a{% u aa %}a", and "aa{% u aa %}".
> It can be shown that the maximum length achievable is 2.

**Example 2:**

> Input: `s = "abcdef"`
> Output: `-1`
> Explanation: There exists no special substring which occurs at least thrice. Hence return -1.

**Example 3:**

> Input: `s = "abcaba"`
> Output: `1`
> Explanation: The longest special substring which occurs thrice is "a": substrings "{% u a %}bcaba", "abc{% u a %}ba", and "abcab{% u a %}".
> It can be shown that the maximum length achievable is 1.

**Constraints:**

- `3 <= s.length <= 50`
- `s` consists of only lowercase English letters.

## Test Cases

```python
class Solution:
    def maximumLength(self, s: str) -> int:
```

{% snippet solution_test.py %}

## Thoughts

首先对于某个字符的一个连续片段（如 `"aaaa"`），若长度为 n，则其中包含「出现至少三次的特殊子字符串」的最长长度为 `n - 2`（如 Example 1 所示）。

如果某字符有两个片段（如 `"aa****aaa"`），设长度分别为 m 和 n（不妨设 `m ≤ n`）。如果 `m < n`，则长为 n 的片段中至少可以出现两次长度为 m 的特殊子字符串，加上长为 m 的片段就可以满足「出现至少三次」。如果 `m = n`，则两个片段中各出现两次长度为 `n - 1` 的特殊子字符串，加起来可以满足「出现至少三次」。

如果某字符有三个片段（如 `"aa***aa***aaa"`），设长度分别为 k、m 和 n（不妨设 `k ≤ m ≤ n`）。如果 `k = m = n`，则显然长为 n 的特殊子字符串满足「出现至少三次」。如果 `k < m ≤ n`，那就对 m 和 n 按上边两个片段的逻辑处理即可。

如果有更多的片段，只需要看最长的两个和三个即可。

总的来看，设某个字符最长的三个片段的长度分别为 k、m 和 n（不妨设 `0 ≤ k ≤ m ≤ n`），那么该字符的「出现至少三次的特殊子字符串」的最长长度为：

$$
\begin{cases}
  n & \text{if }k=m=n \\
  n-1 & \text{if }k<m=n \\
  max(m,n-2) & \text{if }k\le m<n
\end{cases}
$$

遍历 `s`，对每个字符用大小为 3 的最小堆记录最长的三个片段的长度，根据上边式子计算该字符「出现至少三次的特殊子字符串」的最长长度，最后对所有字符取最大即可。

时间复杂度 `O(n)`（这里 n 表示 `s` 的长度），空间复杂度 `O(1)`（实际上是 `s` 中不同字符的数量，题目限定了仅小写英文字符，则可以认为是常数；否则也可以认为是 `O(n)`）。

## Code

{% snippet solution.py %}
