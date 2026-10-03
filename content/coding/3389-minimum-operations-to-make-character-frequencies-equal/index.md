---
title: 3389. Minimum Operations to Make Character Frequencies Equal
notebook: coding
tags:
- hard
katex: true
date: 2024-12-19 18:13:43
updated: 2024-12-19 18:13:43
---
## Problem

You are given a string `s`.

A string `t` is called **good** if all characters of `t` occur the same number of times.

You can perform the following operations **any number of times**:

- Delete a character from `s`.
- Insert a character in `s`.
- Change a character in `s` to its next letter in the alphabet.

**Note** that you cannot change `'z'` to `'a'` using the third operation.

Return the **minimum** number of operations required to make `s` **good**.

<https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/>

**Example 1:**

> Input: `s = "acab"`
> Output: `1`
> Explanation:
> We can make s good by deleting one occurrence of character `'a'`.

**Example 2:**

> Input: `s = "wddw"`
> Output: `0`
> Explanation:
> We do not need to perform any operations since s is initially good.

**Example 3:**

> Input: `s = "aaabc"`
> Output: `2`
> Explanation:
> We can make s good by applying these operations:
>
> - Change one occurrence of `'a'` to `'b'`
> - Insert one occurrence of `'c'` into s

**Constraints:**

- `3 <= s.length <= 2 * 10⁴`
- `s` contains only lowercase English letters.

## Test Cases

```python
class Solution:
    def makeStringGood(self, s: str) -> int:
```

{% snippet solution_test.py %}

## Thoughts

可以进行的三个操作：

1. 删除任意字符。
2. 插入任意字符。
3. 把任意字符替换成其字典序的下一个字符（如 `'a'` 换成 `'b'`）。显然对两个或更多相连的字符做此操作没意义（如 `'a'` 换成 `'b'`，`'b'` 再换成 `'c'`），可以用删除第一个 + 插入最后一个替代。

开始一直想怎么计算出最终 good 状态时，每个字符的个数（记为目标值 t），或者在推导最少操作次数的过程中能自适应更新这个值，未果。只好直接暴力（brute force）枚举所有可能的 t。显然 t 最小为 0，最大不会超过 s 中的最大词频。中间的任何一个值都是有可能的。问题就转变为对于指定的 t，计算出最终词频全为 t（或者 0）的最少操作次数。

首先统计出 s 中每个字符的词频。记 i（`1 ≤ i ≤ 26`）表示按字典序的第 i 个小写字母（简称字符 i），记 `fᵢ` 为字符 i 在 s 中的词频。

记 `ops(i)` 表示把前 i 个字符的词频都调成 t 所需的最少操作次数，同时记录 `del(i)` 表示当 `ops(i)` 最优时，第 i 个字符被删除的个数（用于进行操作 3）。

如果 `fᵢ ≥ t`，那就删掉 `fᵢ - t` 个字符 i 即可，同时 `del(i) = fᵢ - t`。

如果 `fᵢ < t`，那么有两个选择，一个是把 `fᵢ` 个字符 i 全部删光（同时 `del(i) = fᵢ`），另一个是插入 `ins = t - fᵢ` 个字符 i。

插入动作需要考虑是否可以通过操作 3 替代掉一部分，以减少操作次数。这里又有两个选择。

如果前一个字符做了一些删除操作（`del(i - 1) > 0`），可以把其中的一些改成操作 3，剩余的插入次数为 `max{0, ins - del(i - 1)}`。

另一个选择是把前一个字符全部删除（共 `fᵢ₋₁` 次），把其中一些改成操作 3，剩余的插入次数为 `ins' = max{0, ins - fᵢ₋₁}`。总的操作次数相当于在 `ops(i - 2)` 的基础上，增加 `fᵢ₋₁ + ins'` 次。

总结下来，`ops(i)` 和 `del(i)` 的转移方程为：

$$
(ops_i,del_i)=\begin{cases}
  (ops_{i-1}+(f_i-t),f_i-t) & \text{if }f_i\ge t \\
  \min\begin{cases}
    (ops_{i-1}+f_i,f_i) \\
    (ops_{i-1}+\max\{0,t-f_i-del_{i-1}\},0) \\
    (ops_{i-2}+f_{i-1}+\max\{0,t-f_i-f_{i-1}\},0)
  \end{cases}
\end{cases}
$$

其中 ops 只需要保留前两个值，del 只需要保留前一个值，占用 `O(1)` 空间。

设 s 中各不相同的字符共 k 个（按题目限定最多为 26，也可以认为是常数），最大词频为 `F = O(n)`，则时间复杂度 `O(k * n)`，空间复杂度 `O(k)`。

## Code

{% snippet solution.py %}
