---
title: 1769. Minimum Number of Operations to Move All Balls to Each Box
notebook: coding
tags:
- medium
katex: true
date: 2025-01-06 11:41:07
updated: 2025-01-06 11:41:07
---
## Problem

You have `n` boxes. You are given a binary string `boxes` of length `n`, where `boxes[i]` is `'0'` if the `iᵗʰ` box is **empty**, and `'1'` if it contains **one** ball.

In one operation, you can move **one** ball from a box to an adjacent box. Box `i` is adjacent to box `j` if `abs(i - j) == 1`. Note that after doing so, there may be more than one ball in some boxes.

Return an array `answer` of size `n`, where `answer[i]` is the **minimum** number of operations needed to move all the balls to the `ith` box.

Each `answer[i]` is calculated considering the **initial** state of the boxes.

<https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/>

**Example 1:**

> Input: `boxes = "110"`
> Output: `[1,1,3]`
> Explanation: The answer for each box is as follows:
>
> 1) First box: you will have to move one ball from the second box to the first box in one operation.
> 2) Second box: you will have to move one ball from the first box to the second box in one operation.
> 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

**Example 2:**

> Input: `boxes = "001011"`
> Output: `[11,8,5,4,3,4]`

**Constraints:**

- `n == boxes.length`
- `1 <= n <= 2000`
- `boxes[i]` is either `'0'` or `'1'`.

## Test Cases

```python
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
```

{% snippet solution_test.py %}

## Thoughts

先看把所有球都挪到 `i = 0` 需要移动几次。显然位置 j 的球需要移动 j 次。遍历一次 boxes 字符串，所有有球的 j，把 j 累加到移动次数（记为 `moves(0)`）上，同时记录一共有多少个球（记为 nr）。此时位置 0 左边没有球，记 `nl = 0`。

如果已经知道 `moves(i)`，看如何计算 `moves(i + 1)`。对于 **`i + 1`** 左边的所有球（`nl(i + 1)` 个），都需要多移动一步；而 **i** 右边的球（`nr(i)` 个），都可以少移动一步。所以 `moves(i + 1) = moves(i) + nl(i + 1) - nr(i)`。

如果位置 i 原本没有球（`boxes[i] = '0'`），那么 `nl(i + 1) = nl(i)`，`nr(i) = nr(i - 1)`。否则（`boxes[i] = '1'`）`nl(i + 1) = nl(i) + 1`，`nr(i) = nr(i - 1) - 1`。

显然初始时得到的 nl 实际上就是 `nl(0)`，nr 实际上是 `nr(-1)`，而且 `moves(0)` 也同步计算出来了。然后从 `i = 0` 开始遍历，先计算 `nl(i + 1)` 和 `nr(i)`，再计算出 `moves(i + 1)`。

完整的状态转移公式为：

$$
\begin{cases}
  nl(0)=0 \\
  nl(i+1)=\begin{cases}
    nl(i) & \text{if }boxes[i]=`0\text{\textquoteright} \\
    nl(i)+1 & \text{if }boxes[i]=`1\text{\textquoteright}
  \end{cases}
\end{cases}
$$

$$
\begin{cases}
  nr(-1)=\sum_{0\le j<n,\text{ }boxes[j]=`1\text{\textquoteright}}1 \\
  nr(i)=\begin{cases}
    nr(i-1) & \text{if }boxes[i]=`0\text{\textquoteright} \\
    nr(i-1)-1 & \text{if }boxes[i]=`1\text{\textquoteright}
  \end{cases}
\end{cases}
$$

$$
\begin{cases}
  moves(0)=\sum_{0\le j<n,\text{ }boxes[j]=`1\text{\textquoteright}}j \\
  moves(i+1)=moves(i)+nl(i+1)-nr(i)
\end{cases}
$$

递推过程中只需要保留 nl 和 nr 最新的值即可。时间复杂度 `O(n)`，额外的空间复杂度 `O(1)`。

## Code

{% snippet solution.py %}
