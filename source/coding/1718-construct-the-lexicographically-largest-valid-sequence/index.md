---
title: 1718. Construct the Lexicographically Largest Valid Sequence
notebook: coding
tags:
- medium
date: 2025-02-16 17:58:36
updated: 2025-02-16 17:58:36
---
## Problem

Given an integer `n`, find a sequence that satisfies all of the following:

- The integer `1` occurs once in the sequence.
- Each integer between `2` and `n` occurs twice in the sequence.
- For every integer `i` between `2` and `n`, the **distance** between the two occurrences of `i` is exactly `i`.

The **distance** between two numbers on the sequence, `a[i]` and `a[j]`, is the absolute difference of their indices, `|j - i|`.

Return _the **lexicographically largest** sequence__. It is guaranteed that under the given constraints, there is always a solution._

A sequence `a` is lexicographically larger than a sequence `b` (of the same length) if in the first position where `a` and `b` differ, sequence `a` has a number greater than the corresponding number in `b`. For example, `[0,1,9,0]` is lexicographically larger than `[0,1,5,6]` because the first position they differ is at the third number, and `9` is greater than `5`.

<https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/>

**Example 1:**

> Input: `n = 3`
> Output: `[3,1,2,3,2]`
> Explanation: `[2,3,2,1,3]` is also a valid sequence, but `[3,1,2,3,2]` is the lexicographically largest valid sequence.

**Example 2:**

> Input: `n = 5`
> Output: `[5,3,1,4,3,5,2,4,2]`

**Constraints:**

- `1 <= n <= 20`

## Test Cases

``` python
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
```

{% asset_code coding/1718-construct-the-lexicographically-largest-valid-sequence/solution_test.py %}

## Thoughts

用回溯法。

对于 n，结果序列一共有 `2n - 1` 个位置，从最左边开始，取第一个没有放入数字的位置，取尚未放好的最大数字，先看该数字是否可以放的下所有个数（对于大于 1 的数字都需要放在两个位置），如果可以就递归地处理下一个位置，否则就继续看尚未放好的下一个数字。

时间复杂度大约是 `O(n!)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/1718-construct-the-lexicographically-largest-valid-sequence/solution.py %}
