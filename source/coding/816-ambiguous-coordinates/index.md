---
title: 816. Ambiguous Coordinates
notebook: coding
tags:
- medium
date: 2025-01-02 22:42:23
updated: 2025-01-02 22:42:23
---
## Problem

We had some 2-dimensional coordinates, like `"(1, 3)"` or `"(2, 0.5)"`. Then, we removed all commas, decimal points, and spaces and ended up with the string s.

- For example, `"(1, 3)"` becomes `s = "(13)"` and `"(2, 0.5)"` becomes `s = "(205)"`.

Return _a list of strings representing all possibilities for what our original coordinates could have been_.

Our original representation never had extraneous zeroes, so we never started with numbers like `"00"`, `"0.0"`, `"0.00"`, `"1.0"`, `"001"`, `"00.01"`, or any other number that can be represented with fewer digits. Also, a decimal point within a number never occurs without at least one digit occurring before it, so we never started with numbers like `".1"`.

The final answer list can be returned in any order. All coordinates in the final answer have exactly one space between them (occurring after the comma.)

<https://leetcode.com/problems/ambiguous-coordinates/>

**Example 1:**

> Input: `s = "(123)"`
> Output: `["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]`

**Example 2:**

> Input: `s = "(0123)"`
> Output: `["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]`
> Explanation: `0.0`, `00`, `0001` or `00.01` are not allowed.

**Example 3:**

> Input: `s = "(00011)"`
> Output: `["(0, 0.011)","(0.001, 1)"]`

**Constraints:**

- `4 <= s.length <= 12`
- `s[0] == '('` and `s[s.length - 1] == ')'`.
- The rest of `s` are digits.

## Test Cases

``` python
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
```

{% asset_code coding/816-ambiguous-coordinates/solution_test.py %}

## Thoughts

把 s 两头的括号去掉，剩下都是 digits，设 digits 的个数为 n。可以尝试在所有的位置把 s 分成左右两半，每半至少包含一个 digit。枚举每一半可以构造的有效的数值（有可能一个都没有），左右两半的可行数值数组取笛卡尔积可以得到所有可行的组合。

对于一个由若干个 digits 构成的字符串，看它可以构造出哪些合法的数值。

首先如果只有一个 digit，那么只能构成一个一位整数。

否则如果不以 `'0'` 开头，那么整体可以构成一个整数。然后看可以构成的小数有哪些。

如果末尾是 `'0'`，就无法构成任何有效的小数数值。否则如果以 `'0'` 开头，那么只能构成 `0.xxx` 这样的唯一一个小数。其他情况下，都可以给任意中间位置插入小数点构成一个小数，都是有效的。

时间复杂度 `O(n²)`。

## Code

{% asset_code coding/816-ambiguous-coordinates/solution.py %}
