---
title: 3292. Minimum Number of Valid Strings to Form Target II
notebook: coding
tags:
- hard
date: 2024-12-17 16:17:12
updated: 2024-12-18 16:23:05
---
[3291. Minimum Number of Valid Strings to Form Target I](../3291-minimum-number-of-valid-strings-to-form-target-i/index.md) 的进阶版，题目一模一样，但 words 的长度从 `5 * 10³` 增加到 `5 * 10⁵`，target 的长度从 `5 * 10³` 增加到 `5 * 10⁴`。

如果按 [problem 3291](../3291-minimum-number-of-valid-strings-to-form-target-i/index.md) 中 `O(n²)` 复杂度的 trie 树 + 动态规划是无法 AC 的，需要用更快的 [AC 自动机](../3291-minimum-number-of-valid-strings-to-form-target-i/index.md#Faster-AC-自动机)。
