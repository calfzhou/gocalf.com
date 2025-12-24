---
title: 1639. Number of Ways to Form a Target String Given a Dictionary
notebook: coding
tags:
- hard
katex: true
date: 2024-12-29 20:43:54
updated: 2024-12-29 20:43:54
---
## Problem

You are given a list of strings of the **same length** `words` and a string `target`.

Your task is to form `target` using the given `words` under the following rules:

- `target` should be formed from left to right.
- To form the `iᵗʰ` character (**0-indexed**) of `target`, you can choose the `kᵗʰ` character of the `jᵗʰ` string in `words` if `target[i] = words[j][k]`.
- Once you use the `kᵗʰ` character of the `jᵗʰ` string of `words`, you **can no longer** use the `xᵗʰ` character of any string in `words` where `x <= k`. In other words, all characters to the left of or at index `k` become unusuable for every string.
- Repeat the process until you form the string `target`.

**Notice** that you can use **multiple characters** from the **same string** in `words` provided the conditions above are met.

Return _the number of ways to form `target` from `words`_. Since the answer may be too large, return it **modulo** `10⁹ + 7`.

<https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/>

**Example 1:**

> Input: `words = ["acca","bbbb","caca"], target = "aba"`
> Output: `6`
> Explanation: There are 6 ways to form target.
> "aba" -> index 0 ("{% u a %}cca"), index 1 ("b{% u b %}bb"), index 3 ("cac{% u a %}")
> "aba" -> index 0 ("{% u a %}cca"), index 2 ("bb{% u b %}b"), index 3 ("cac{% u a %}")
> "aba" -> index 0 ("{% u a %}cca"), index 1 ("b{% u b %}bb"), index 3 ("acc{% u a %}")
> "aba" -> index 0 ("{% u a %}cca"), index 2 ("bb{% u b %}b"), index 3 ("acc{% u a %}")
> "aba" -> index 1 ("c{% u a %}ca"), index 2 ("bb{% u b %}b"), index 3 ("acc{% u a %}")
> "aba" -> index 1 ("c{% u a %}ca"), index 2 ("bb{% u b %}b"), index 3 ("cac{% u a %}")

**Example 2:**

> Input: `words = ["abba","baab"], target = "bab"`
> Output: `4`
> Explanation: There are 4 ways to form target.
> "bab" -> index 0 ("{% u b %}aab"), index 1 ("b{% u a %}ab"), index 2 ("ab{% u b %}a")
> "bab" -> index 0 ("{% u b %}aab"), index 1 ("b{% u a %}ab"), index 3 ("baa{% u b %}")
> "bab" -> index 0 ("{% u b %}aab"), index 2 ("ba{% u a %}b"), index 3 ("baa{% u b %}")
> "bab" -> index 1 ("a{% u b %}ba"), index 2 ("ba{% u a %}b"), index 3 ("baa{% u b %}")

**Constraints:**

- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 1000`
- All strings in `words` have the same length.
- `1 <= target.length <= 1000`
- `words[i]` and `target` contain only lowercase English letters.

## Test Cases

``` python
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
```

{% asset_code coding/1639-number-of-ways-to-form-a-target-string-given-a-dictionary/solution_test.py %}

## Thoughts

设 words 中每个 word 的长度为 n，target 长度为 m。显然若 `m > n` 则怎么都拼不出 target，返回 0。

首先统计 words 中每个字符位置 j（`0 ≤ j < n`），不同字符 c（`"a" ≤ c ≤ "z"`）的可选次数，记为 `occ(j, c)`。其值为 words 中，`jᵗʰ` 字符是 c 的 word 个数。比如 Example 1 中 `words = ["acca","bbbb","caca"]` 可以得到如下的 occ 表：

| c   | 0 | 1 | 2 | 3 |
|-----|---|---|---|---|
| "a" | 1 | 1 | 0 | 2 |
| "b" | 1 | 1 | 1 | 1 |
| "c" | 1 | 1 | 2 | 0 |

对于 target 中的每个位置 i（`0 ≤ i < m`），最多可以从 word 的 `n' = n - m + 1` 个字符位置（即 `[i, i + n - m + 1]`）中选择，因为要给 i 前后的其他位置留下选择的空间。对于 i（`0 ≤ i < m`）和 j（`i ≤ j ≤ i + n - m + 1`），可选的 word 数量为 `occ(j, target[i])`。

为了方便，可以把每个 i 的可选区间左对齐，得到一个 m 行 `n'` 列的 grid（如下图）。用 `j'` 表示可选区间的第 `j'` 个位置，其对应于第 `(i + j')`ᵗʰ 字符，格子内的数值为 `occ(i+j', target[i])`。。

{% invert %}
{% diagramsnet choose-from.drawio %}
{% endinvert %}

对每一行做出选择，但每一行选的 `j'` 都不能小于上一行所选的 `j'`。这就相当于从上图右边 grid 的左上角，只能向右或向下移动，最终走到右下角，看有多少种走法。跟 [62. Unique Paths](../62-unique-paths/index.md) 是一样的，只不过每个格子都带上了「系数」。

看其中任意一条路径对应多少种选择。为了方便，在 grid 上方加一个空行，并将起点定为空行的第一个格子，这样一共需要向下走 m 次。每次向下走到第 i 行就表示为 target 的第 i 个字符确定了字符的来源（如此时位于 `j'` 列，则 target 的第 i 个字符是从其第 `j'` 个可选位置的某个 word 来的）。而向右走只是为了能够在右边某一列向下走做的准备，不代表实际的选择。这样一条路径对应的选择数量，就是每次向下走时经过的格子的数字之积。

如下图的蓝色路径，三次向下走到达的格子坐标分别为 `(0, 0)`、`(1, 0)` 和 `(2, 1)`，对应于 `occ(0+0, "a") = 1`、`occ(1+0, "b") = 1` 和 `occ(2+1, "a") = 2`，共 `1 * 1 * 2 = 2` 个选择。

{% invert %}
{% diagramsnet one-path.drawio %}
{% endinvert %}

把所有路径的选择数累加起来，就是最终的结果。

定义 `dp(i, j')` 表示到 `(i, j')` 格子的所有路径的选择数总和。要走到 `(i, j')`，可以从上边 `(i-1, j')` 或者左边 `(i, j'-1)` 过来。从上边过来的时候，需要乘以 `(i, j')` 格子的数字（`occ(i+j, target[i])`）；从左边过来时乘以 1 即可。所以：

$$
dp(i,j')=dp(i-1,j')\times occ(i+j, target[i])+dp(i,j'-1)
$$

为了简化边界的处理，可以定义 `dp(i, -1) = 1`（即上方增加的空行），`dp(-1, j') = 0`。最终结果为 `dp(m - 1, n' - 1)`。

跟 [62. Unique Paths](../62-unique-paths/index.md) 类似，dp 在递推过程中只需要保留最新的一行（或一列）即可。

时间复杂度 `O(W * n + m * (n - m))`，空间复杂度 `O(C * n + (n - m))`，其中 W 是 words 的长度，C 是各不相同的字符数（题目中最多 26，可以认为是常数）。

## Code

{% asset_code coding/1639-number-of-ways-to-form-a-target-string-given-a-dictionary/solution.py %}
