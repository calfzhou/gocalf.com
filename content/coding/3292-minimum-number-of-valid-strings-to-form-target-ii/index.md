---
title: 3292. Minimum Number of Valid Strings to Form Target II
tags:
- hard
date: "2024-12-17T16:17:12+08:00"
lastmod: "2024-12-18T16:23:05+08:00"
---
[3291. Minimum Number of Valid Strings to Form Target I](../3291-minimum-number-of-valid-strings-to-form-target-i/index.md) 的进阶版，题目一模一样，但 words 的长度从 `5 * 10³` 增加到 `5 * 10⁵`，target 的长度从 `5 * 10³` 增加到 `5 * 10⁴`。

如果按 [problem 3291](../3291-minimum-number-of-valid-strings-to-form-target-i/index.md) 中 `O(n²)` 复杂度的 trie 树 + 动态规划是无法 AC 的，需要用更快的 [AC 自动机](../3291-minimum-number-of-valid-strings-to-form-target-i/index.md#faster---ac-%E8%87%AA%E5%8A%A8%E6%9C%BA)。
