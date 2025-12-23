---
title: 1079. Letter Tile Possibilities
notebook: coding
tags:
- medium
date: 2025-02-17 16:01:51
updated: 2025-02-17 16:01:51
---
## Problem

You have `n` `tiles`, where each tile has one letter `tiles[i]` printed on it.

Return _the number of possible non-empty sequences of letters_ you can make using the letters printed on those `tiles`.

<https://leetcode.com/problems/letter-tile-possibilities/>

**Example 1:**

> Input: `tiles = "AAB"`
> Output: `8`
> Explanation: The possible sequences are `"A"`, `"B"`, `"AA"`, `"AB"`, `"BA"`, `"AAB"`, `"ABA"`, `"BAA"`.

**Example 2:**

> Input: `tiles = "AAABBC"`
> Output: `188`

**Example 3:**

> Input: `tiles = "V"`
> Output: `1`

**Constraints:**

- `1 <= tiles.length <= 7`
- `tiles` consists of uppercase English letters.

## Test Cases

``` python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
```

{% asset_code coding/1079-letter-tile-possibilities/solution_test.py %}

## Thoughts

相当于 [90. Subsets II](../90-subsets-ii/index.md) 和 [47. Permutations II](../47-permutations-ii/index.md) 的组合拳，先用 [90. Subsets II](../90-subsets-ii/index.md) 的方法找出所有（各个长度的）子集合，然后用 [47. Permutations II](../47-permutations-ii/index.md) 的方法计算该子集合所有排列。不过本题不需要枚举所有的子集合的所有排列，只需要计算总数。

[90. Subsets II](../90-subsets-ii/index.md) 的代码基本可以直接搬过来用，只是在把枚举到的子集加入结果列表的地方改成计算该子集的排列数。另外因为具体的字符并不重要，只关心该字符在子集合中出现多少次，可以用 occurs 替代 subset，即只记录 subset 中各个字符的出现次数。

对于一个长度为 m 的子集合，其总的排列数可以直接用数学方法计算出来，即用 m 的阶乘除以每一个字符的次数的阶乘，不需要套用 [47. Permutations II](../47-permutations-ii/index.md) 的回溯逻辑。时间复杂度为 `O(m)`。

所以总的时间复杂度跟 [90. Subsets II](../90-subsets-ii/index.md) 一样，都是 `O(2^n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/1079-letter-tile-possibilities/solution.py %}
