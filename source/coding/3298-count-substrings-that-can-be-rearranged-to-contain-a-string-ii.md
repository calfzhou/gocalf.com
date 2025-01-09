---
title: 3298. Count Substrings That Can Be Rearranged to Contain a String II
notebook: coding
tags:
- hard
date: 2025-01-09 10:25:43
updated: 2025-01-09 10:25:43
---
## Problem

跟 [3297. Count Substrings That Can Be Rearranged to Contain a String I](3297-count-substrings-that-can-be-rearranged-to-contain-a-string-i) 一模一样，只是多了一个注意点：

**Note** that the memory limits in this problem are **smaller** than usual, so you **must** implement a solution with a _linear_ runtime complexity.

<https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/>

## Thoughts

[Problem 3297](3297-count-substrings-that-can-be-rearranged-to-contain-a-string-i) 的时间复杂度 `O(n + m)`（n 和 m 分别是 word1 和 word2 的长度），空间复杂度 `O(k) ≈ O(1)`（k 是 word2 中不同字符的个数）。基本符合本题的限制，可以直接用。
