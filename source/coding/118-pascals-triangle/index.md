---
title: 118. Pascal’s Triangle
notebook: coding
tags:
- easy
date: 2025-01-28 21:46:19
updated: 2025-01-28 21:46:19
---
## Problem

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

<https://leetcode.cn/problems/pascals-triangle/>

![pascal|240](../119-pascals-triangle-ii/pascal.gif "pascal"){.invert-when-dark}

**Example 1:**

> Input: `numRows = 5`
> Output: `[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`

**Example 2:**

> Input: `numRows = 1`
> Output: `[[1]]`

**Constraints:**

- `1 <= numRows <= 30`

## Test Cases

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
```

{% asset_code coding/118-pascals-triangle/solution_test.py %}

## Thoughts

直接用 [119. Pascal's Triangle II](../119-pascals-triangle-ii/index.md) 中组合数的递推方式计算整个杨辉三角即可。

## Code

{% asset_code coding/118-pascals-triangle/solution.py %}
