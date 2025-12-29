---
title: 3174. Clear Digits
notebook: coding
tags:
- easy
date: 2025-02-10 10:07:28
updated: 2025-02-10 10:07:28
---
## Problem

You are given a string `s`.

Your task is to remove **all** digits by doing this operation repeatedly:

- Delete the _first_ digit and the **closest** **non-digit** character to its _left_.

Return the resulting string after removing all digits.

<https://leetcode.com/problems/clear-digits/>

**Example 1:**

> Input: `s = "abc"`
> Output: `"abc"`
> Explanation:
> There is no digit in the string.

**Example 2:**

> Input: `s = "cb34"`
> Output: `""`
> Explanation:
> First, we apply the operation on `s[2]`, and s becomes `"c4"`.
> Then we apply the operation on `s[1]`, and s becomes `""`.

**Constraints:**

- `1 <= s.length <= 100`
- `s` consists only of lowercase English letters and digits.
- The input is generated such that it is possible to delete all digits.

## Test Cases

```python
class Solution:
    def clearDigits(self, s: str) -> str:
```

{% asset_code coding/3174-clear-digits/solution_test.py %}

## Thoughts

用一个栈记录结果字符串的字符。

遍历 s 的每一个字符，如果不是数字则压栈，如果是数字则从栈里弹出最后一个字符即可。

时间复杂度 `O(n)`，附加的空间复杂度 `O(n)`。

## Code

{% asset_code coding/3174-clear-digits/solution.py %}
