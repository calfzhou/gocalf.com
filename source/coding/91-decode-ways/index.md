---
title: 91. Decode Ways
notebook: coding
tags:
- medium
katex: true
date: 2024-11-23 14:13:06
updated: 2024-11-23 14:13:06
---
## Problem

You have intercepted a secret message encoded as a string of numbers. The message is **decoded** via the following mapping:

`"1" -> 'A'   "2" -> 'B'   ...   "25" -> 'Y'   "26" -> 'Z'`

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

- `"AAJF"` with the grouping `(1, 1, 10, 6)`
- `"KJF"` with the grouping `(11, 10, 6)`
- The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the **number of ways** to **decode** it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a **32-bit** integer.

<https://leetcode.com/problems/decode-ways/>

**Example 1:**

> Input: `s = "12"`
> Output: `2`
> Explanation:
> `"12"` could be decoded as `"AB"` `(1 2)` or `"L"` `(12)`.

**Example 2:**

> Input: `s = "226"`
> Output: `3`
> Explanation:
> `"226"` could be decoded as `"BZ"` `(2 26)`, `"VF"` `(22 6)`, or `"BBF"` `(2 2 6)`.

**Example 3:**

> Input: `s = "06"`
> Output: `0`
> Explanation:
> `"06"` cannot be mapped to `"F"` because of the leading zero (`"6"` is different from `"06"`). In this case, the string is not a valid encoding, so return 0.

**Constraints:**

- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zero(s).

## Test Cases

```python
class Solution:
    def numDecodings(self, s: str) -> int:
```

{% snippet solution_test.py %}

## Thoughts

相当于是 [70. Climbing Stairs](../70-climbing-stairs/index.md) 的进阶版，想象每个台阶上写了一个数字。只不过增加了限制，只有满足条件的一个或两个台阶才能迈过。

定义 `w[i]` 是数字子串 `s[0:i+1]` 可行的解码方案总数。

子串 `s[0:i+1]` 可以是在 `s[0:i]` 的基础上添加 `s[i]`，除非 `s[i] = "0"`。

另外子串 `s[0:i+1]` 还可以是在 `s[0:i-1]` 的基础上添加 `s[i-1:i+1]` 两个数字，除非 `s[i-1:i+1]` 不是 `"10"` 到 `"26"`。

所以：

$$
\begin{array}{rl}
  w[i]&=\begin{cases}
    w[i-1] &\text{if \textquotedblleft 1"}\le s[i]\le\text{\textquotedblleft 9"} \\
    0 &\text{otherwise}
  \end{cases} \\
  \\
  &+\begin{cases}
    w[i-2] &\text{if \textquotedblleft 10"}\le s[i-1:i+1]\le\text{\textquotedblleft 26"} \\
    0 &\text{otherwise}
  \end{cases}
\end{array}
$$

初始值为：

$$
w[0]=\begin{cases}
  1 &\text{if \textquotedblleft 1"}\le s[0]\le\text{\textquotedblleft 9"} \\
  0 &\text{otherwise}
\end{cases}
$$

显然如果 `w[0]` 是 0，或者连续两个 `w` 的值是 0，最终结果一定为 0。

## Code

{% snippet solution.py %}
