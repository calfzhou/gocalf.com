---
title: 3083. Existence of a Substring in a String and Its Reverse
notebook: coding
tags:
- easy
date: 2024-12-26 00:24:14
updated: 2024-12-26 00:24:14
---
## Problem

Given a string `s`, find any substring of length `2` which is also present in the reverse of `s`.

> A **substring** is a contiguous sequence of characters within a string.

Return `true` _if such a substring exists, and_ `false` _otherwise._

<https://leetcode.cn/problems/existence-of-a-substring-in-a-string-and-its-reverse/>

**Example 1:**

> Input: `s = "leetcode"`
> Output: `true`
> Explanation: Substring `"ee"` is of length 2 which is also present in `reverse(s) == "edocteel"`.

**Example 2:**

> Input: `s = "abcba"`
> Output: `true`
> Explanation: All of the substrings of length 2 `"ab"`, `"bc"`, `"cb"`, `"ba"` are also present in `reverse(s) == "abcba"`.

**Example 3:**

> Input: `s = "abcd"`
> Output: `false`
> Explanation: There is no substring of length 2 in s, which is also present in the reverse of s.

**Constraints:**

- `1 <= s.length <= 100`
- `s` consists only of lowercase English letters.

## Test Cases

``` python
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
```

{% asset_code coding/assets/3083-existence-of-a-substring-in-a-string-and-its-reverse/solution_test.py %}

## Thoughts

扫描 s 中所有长度为 2 的子字符串，加入哈希集合。同时检查这个子字符串翻转之后是否也在集合中，在就返回 true。

显然并不用先把所有长度为 2 的子字符串都添加完再做判定，可以一边加一边比较。

## Code

{% asset_code coding/assets/3083-existence-of-a-substring-in-a-string-and-its-reverse/solution.py %}
