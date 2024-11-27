---
title: 633. Sum of Square Numbers
notebook: coding
tags:
- medium
date: 2024-11-27 11:12:54
updated: 2024-11-27 11:12:54
---
## Problem

Given a non-negative integer `c`, decide whether there're two integers `a` and `b` such that `a² + b² = c`.

<https://leetcode.cn/problems/sum-of-square-numbers/>

**Example 1:**

> Input: `c = 5`
> Output: `true`
> Explanation: `1 * 1 + 2 * 2 = 5`

**Example 2:**

> Input: `c = 3`
> Output: `false`

**Constraints:**

- `0 <= c <= 2^31 - 1`

## Test Cases

``` python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
```

{% asset_code coding/633-sum-of-square-numbers/solution_test.py %}

## Thoughts

不妨设 `a <= b`。显然 b 最大不会超过 `√c`，a 最小可以是 0。这时候如果 `a² + b²` 刚好等于 c，说明 c 是平方和。否如根据当前平方和与 c 的大小关系，自增 a 或者自减 b 之后继续比对。

也可以直接从 `a = 0` 开始，每次判断 `c - a²` 是否是平方数，直到 a 比后者更大。

## Code

{% asset_code coding/633-sum-of-square-numbers/solution.py %}
