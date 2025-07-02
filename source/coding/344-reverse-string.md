---
title: 344. Reverse String
notebook: coding
tags:
- easy
date: 2025-01-31 21:36:27
updated: 2025-01-31 21:36:27
---
## Problem

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with `O(1)` extra memory.

<https://leetcode.cn/problems/reverse-string/>

**Example 1:**

> Input: `s = ["h","e","l","l","o"]`
> Output: `["o","l","l","e","h"]`

**Example 2:**

> Input: `s = ["H","a","n","n","a","h"]`
> Output: `["h","a","n","n","a","H"]`

**Constraints:**

- `1 <= s.length <= 10⁵`
- `s[i]` is a [printable ascii character](https://en.wikipedia.org/wiki/ASCII#Printable_characters).

## Test Cases

``` python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
```

{% asset_code coding/assets/344-reverse-string/solution_test.py %}

## Thoughts

用两个指针分别指向数组的首尾，交换两个指针的字符，然后向中间移动指针，直到二者相遇。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/assets/344-reverse-string/solution.py %}
