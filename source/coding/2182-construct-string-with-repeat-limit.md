---
title: 2182. Construct String With Repeat Limit
notebook: coding
tags:
- medium
date: 2024-12-17 10:43:41
updated: 2024-12-17 10:43:41
---
## Problem

You are given a string `s` and an integer `repeatLimit`. Construct a new string `repeatLimitedString` using the characters of `s` such that no letter appears **more than** `repeatLimit` times **in a row**. You do **not** have to use all characters from `s`.

Return _the **lexicographically largest**_ `repeatLimitedString` _possible_.

A string `a` is **lexicographically larger** than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears later in the alphabet than the corresponding letter in `b`. If the first `min(a.length, b.length)` characters do not differ, then the longer string is the lexicographically larger one.

<https://leetcode.com/problems/construct-string-with-repeat-limit/>

**Example 1:**

> Input: `s = "cczazcc", repeatLimit = 3`
> Output: `"zzcccac"`
> Explanation: We use all of the characters from s to construct the repeatLimitedString `"zzcccac"`.
> The letter `'a'` appears at most 1 time in a row.
> The letter `'c'` appears at most 3 times in a row.
> The letter `'z'` appears at most 2 times in a row.
> Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
> The string is the lexicographically largest repeatLimitedString possible so we return `"zzcccac"`.
> Note that the string `"zzcccca"` is lexicographically larger but the letter `'c'` appears more than 3 times in a row, so it is not a valid repeatLimitedString.

**Example 2:**

> Input: `s = "aababab", repeatLimit = 2`
> Output: `"bbabaa"`
> Explanation: We use only some of the characters from s to construct the repeatLimitedString `"bbabaa"`.
> The letter `'a'` appears at most 2 times in a row.
> The letter `'b'` appears at most 2 times in a row.
> Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
> The string is the lexicographically largest repeatLimitedString possible so we return `"bbabaa"`.
> Note that the string `"bbabaaa"` is lexicographically larger but the letter `'a'` appears more than 2 times in a row, so it is not a valid repeatLimitedString.

**Constraints:**

- `1 <= repeatLimit <= s.length <= 10⁵`
- `s` consists of lowercase English letters.

## Test Cases

``` python
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
```

{% asset_code coding/assets/2182-construct-string-with-repeat-limit/solution_test.py %}

## Thoughts

先用 [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) 或类似的哈希表结构，记录 s 中每个字符出现的总次数（每个字符在 s 中的位置信息完全不需要了）。

然后对所有各不相同的字符按照字典顺序逆序排列，因为限定了只有小写英文字符，这个时间可以认为是常数。

从最大的字符开始，如果剩余的次数够多就只取 `repeatLimitedString` 次，然后加一个剩余字符中最大的字符作为隔断。否则就把全都取走。

如果当前最大的字符剩余的次数大于 `repeatLimitedString`，但是没有更小的其他字符了，就不能继续添加了。这也就是题目中说的「不是必须用掉 s 中的所有字符」。

时间复杂度大约是 `O(n)`（或者算 `O(n / repeatLimit)`），空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/2182-construct-string-with-repeat-limit/solution.py %}
