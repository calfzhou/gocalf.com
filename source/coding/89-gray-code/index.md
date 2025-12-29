---
title: 89. Gray Code
notebook: coding
tags:
- medium
date: 2024-12-20 23:15:33
updated: 2024-12-20 23:15:33
---
## Problem

An **n-bit gray code sequence** is a sequence of `2ⁿ` integers where:

- Every integer is in the **inclusive** range `[0, 2ⁿ - 1]`,
- The first integer is `0`,
- An integer appears **no more than once** in the sequence,
- The binary representation of every pair of **adjacent** integers differs by **exactly one bit**, and
- The binary representation of the **first** and **last** integers differs by **exactly one bit**.

Given an integer `n`, return _any valid **n-bit gray code sequence**_.

<https://leetcode.com/problems/gray-code/>

**Example 1:**

> Input: `n = 2`
> Output: `[0,1,3,2]`
> Explanation:
> The binary representation of `[0,1,3,2]` is `[00,01,11,10]`.
>
> - 0{% u 0 %} and 0{% u 1 %} differ by one bit
> - {% u 0 %}1 and {% u 1 %}1 differ by one bit
> - 1{% u 1 %} and 1{% u 0 %} differ by one bit
> - {% u 1 %}0 and {% u 0 %}0 differ by one bit
>
> `[0,2,3,1]` is also a valid gray code sequence, whose binary representation is `[00,10,11,01]`.
>
> - {% u 0 %}0 and {% u 1 %}0 differ by one bit
> - 1{% u 0 %} and 1{% u 1 %} differ by one bit
> - {% u 1 %}1 and {% u 0 %}1 differ by one bit
> - 0{% u 1 %} and 0{% u 0 %} differ by one bit

**Example 2:**

> Input: `n = 1`
> Output: `[0,1]`

**Constraints:**

- `1 <= n <= 16`

## Test Cases

```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
```

{% asset_code coding/89-gray-code/solution_test.py %}

## Thoughts

格雷编码序列，两个连续的数值仅有一个（二进制）位数的差异。

如果已经得到了 `n - 1` 的格雷编码序列 `[g₁, g₂, ..., gₘ]`（`m = 2ⁿ⁻¹`），其中每个数字的第 n 个二进制位都一定是 0。可以把每个数字的第 n 个二进制位都置为 1，得到新的序列 `[g'₁, g'₂, ..., g'ₘ]`，显然新序列中任意两个连续的数值都仅有一个位数的差异。把第二个序列逆序拼接到第一序列后边，得到 `[g₁, g₂, ..., gₘ, g'ₘ, g'ₘ₋₁, ..., g'₂, g'₁]`，这就是 n 的格雷编码序列。

初始时 `n = 0` 的格雷编码序列就是 `[0]`。

## Code

{% asset_code coding/89-gray-code/solution.py %}
