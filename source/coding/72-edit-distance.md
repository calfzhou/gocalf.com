---
title: 72. Edit Distance
notebook: coding
tags:
- medium
katex: true
date: 2024-12-20 22:15:17
updated: 2024-12-20 22:15:17
---
## Problem

Given two strings `word1` and `word2`, return _the minimum number of operations required to convert `word1` to `word2`_.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

<https://leetcode.com/problems/edit-distance/>

**Example 1:**

> Input: `word1 = "horse", word2 = "ros"`
> Output: `3`
> Explanation:
> horse -> rorse (replace 'h' with 'r')
> rorse -> rose (remove 'r')
> rose -> ros (remove 'e')

**Example 2:**

> Input: `word1 = "intention", word2 = "execution"`
> Output: `5`
> Explanation:
> intention -> inention (remove 't')
> inention -> enention (replace 'i' with 'e')
> enention -> exention (replace 'n' with 'x')
> exention -> exection (replace 'n' with 'c')
> exection -> execution (insert 'u')

**Constraints:**

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## Test Cases

``` python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
```

{% asset_code coding/72-edit-distance/solution_test.py %}

## Thoughts

动态规划的经典问题。

定义 `dp(i, j)` 表示子字符串 `word1[:i]` 和 `word2[:j]` 的编辑距离。

如果 `word1ᵢ = word2ⱼ`，那么这一对字符不用编辑，距离与 `word1[:i-1]` 和 `word2[:j-1]` 的距离相等。

否则就可以尝试不同的编辑操作：

- 在 `word1[:i]` 和 `word2[:j-1]` 基础上，给 `word1` 在 i 之后插入 `word2ⱼ`。
- 删除 `word1ᵢ`，变成 `word1[:i-1]` 和 `word2[:j]`。
- 在 `word1[:i-1]` 和 `word2[:j-1]` 基础上，把 `word1ᵢ` 改成 `word2ⱼ`。

所以状态转移方程为：

$$
dp(i,j)=\begin{cases}
  dp(i-1,j-1) & \text{if }word1_i=word2_j \\
  1+\min\begin{cases}
    dp(i,j-1) & \text{(insert)} \\
    dp(i-1,j) & \text{(delete)} \\
    dp(i-1,j-1) & \text{(replace)}
  \end{cases} & \text{otherwise}
\end{cases}
$$

初始值 `dp(i, 0) = i`，`dp(0, j) = j`。最终 word1 和 word2 的编辑距离为 `dp(m, n)`（其中 m、n 分别为 word1、word2 的长度）。

时间复杂度 `O(m * n)`，空间复杂度 `O(m * n)`。

不过因为最多只需要临近的三个值，就可以只保存 dp 的一行，空间复杂度降为 `O(min{m, n})`。

## Code

### `O(min{m, n})` Space

{% asset_code coding/72-edit-distance/solution.py %}

### `O(m * n)` Space

{% asset_code coding/72-edit-distance/solution2.py %}
