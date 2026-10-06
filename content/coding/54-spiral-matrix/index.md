---
title: 54. Spiral Matrix
tags:
- medium
date: "2024-11-18T18:41:17+08:00"
lastmod: "2024-11-18T18:41:17+08:00"
---
## Problem

Given an `m x n` `matrix`, return _all elements of the_ `matrix` _in spiral order_.

<https://leetcode.com/problems/spiral-matrix/>

**Example 1:**

![case1](case1.png)
{.invert-when-dark}

> Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`\
> Output: `[1,2,3,6,9,8,7,4,5]`

**Example 2:**

![case2](case2.png)
{.invert-when-dark}

> Input: `matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`\
> Output: `[1,2,3,4,8,12,11,10,9,5,6,7]`

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Test Cases

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
```

{{< snippet src="solution_test.py" >}}

## Thoughts

主要就是注意控制好边界。

## Code

{{< snippet src="solution.py" >}}
