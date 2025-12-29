---
title: 1792. Maximum Average Pass Ratio
notebook: coding
tags:
- medium
katex: true
date: 2024-12-15 20:10:53
updated: 2024-12-15 20:10:53
---
## Problem

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array `classes`, where `classes[i] = [passᵢ, totalᵢ]`. You know beforehand that in the `iᵗʰ` class, there are `totalᵢ` total students, but only `passᵢ` number of students will pass the exam.

You are also given an integer `extraStudents`. There are another `extraStudents` brilliant students that are **guaranteed** to pass the exam of any class they are assigned to. You want to assign each of the `extraStudents` students to a class in a way that **maximizes** the **average** pass ratio across **all** the classes.

The **pass ratio** of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The **average pass ratio** is the sum of pass ratios of all the classes divided by the number of the classes.

Return _the **maximum** possible average pass ratio after assigning the_ `extraStudents` _students._ Answers within `10⁻⁵` of the actual answer will be accepted.

<https://leetcode.com/problems/maximum-average-pass-ratio/>

**Example 1:**

> Input: `classes = [[1,2],[3,5],[2,2]], extraStudents = 2`
> Output: `0.78333`
> Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to `(3/4 + 3/5 + 2/2) / 3 = 0.78333`.

**Example 2:**

> Input: `classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4`
> Output: `0.53485`

**Constraints:**

- `1 <= classes.length <= 10⁵`
- `classes[i].length == 2`
- `1 <= passᵢ <= totalᵢ <= 10⁵`
- `1 <= extraStudents <= 10⁵`

## Test Cases

```python
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
```

{% asset_code coding/1792-maximum-average-pass-ratio/solution_test.py %}

## Thoughts

求最大的平均通过率，也可以先计算最小的平均不通过率。记 `pᵢ = passᵢ`、`tᵢ = totalᵢ`、`fᵢ = totalᵢ - passᵢ`，记给第 i 个班加入 `eᵢ` 个「必过学生」，那么：

$$
\begin{array}{rl}
  & \max_{\{e_1,e_2,\dots,e_n\}}\bar{pr} \\
  = & \frac{1}{n}\max_{\{e_1,e_2,\dots,e_n\}}\sum_{i=1}^{n}{(p_i+e_i)/(t_i+e_i)} \\
  = & 1-\frac{1}{n}\min_{\{e_1,e_2,\dots,e_n\}}\sum_{i=1}^{n}{f_i/(t_i+e_i)}
\end{array}
$$

对于任何一个班，只要 `fᵢ ≠ 0`，加入「必过学生」就一定能提高通过率（降低不通过率）。关键是给每个班分配多大的 `eᵢ`。

想看看有没有更「数学」的方法，但没推导出来。只好对「必过学生」一个一个地选择放到哪个班。

假设把一个「必过学生」放进某个班，看能降低多少不通过率，即 $f_i/t_i-f_i/(t_i+1)$。对所有的班级，取这个值最大的即可。

用最大堆记录所有班「加入一个必过学生能降低多少不通过率」，每次取堆顶的班，加入一个「必过学生」后再重新放入堆中。

时间复杂度 `O((n + k) log n)`，其中 `k = extraStudents`。空间复杂度 `O(n)`。

## Code

{% asset_code coding/1792-maximum-average-pass-ratio/solution.py %}
