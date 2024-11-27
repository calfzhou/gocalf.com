---
title: 1957. Delete Characters to Make Fancy String
notebook: coding
tags:
- easy
date: 2024-11-27 18:50:03
updated: 2024-11-27 18:50:03
---
## Problem

A **fancy string** is a string where no **three** **consecutive** characters are equal.

Given a string `s`, delete the **minimum** possible number of characters from `s` to make it **fancy**.

Return _the final string after the deletion_. It can be shown that the answer will always be **unique**.

<https://leetcode.com/problems/delete-characters-to-make-fancy-string/>

**Example 1:**

> Input: `s = "le`{%u e %}`etcode"`
> Output: `"leetcode"`
> Explanation:
> Remove an 'e' from the first group of 'e's to create "leetcode".
> No three consecutive characters are equal, so return "leetcode".

**Example 2:**

> Input: `s = "`{%u a %}`aab`{%u aa %}`aa"`
> Output: `"aabaa"`
> Explanation:
> Remove an 'a' from the first group of 'a's to create "aabaaaa".
> Remove two 'a's from the second group of 'a's to create "aabaa".
> No three consecutive characters are equal, so return "aabaa".

**Example 3:**

> Input: `s = "aab"`
> Output: `"aab"`
> Explanation: No three consecutive characters are equal, so return "aab".

**Constraints:**

- `1 <= s.length <= 10⁵`
- `s` consists only of lowercase English letters.

## Test Cases

``` python
class Solution:
    def makeFancyString(self, s: str) -> str:
```

{% asset_code coding/1957-delete-characters-to-make-fancy-string/solution_test.py %}

## Thoughts

跟 [3206. Alternating Groups I](/coding/3206-alternating-groups-i) 差不多，只是数组首尾不再相接，判定条件从颜色交替变为字符相同。

## Code

{% asset_code coding/1957-delete-characters-to-make-fancy-string/solution.py %}
