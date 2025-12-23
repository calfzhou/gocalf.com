---
title: 2545. Sort the Students by Their Kth Score
notebook: coding
tags:
- medium
date: 2024-12-21 00:44:53
updated: 2024-12-21 00:44:53
---
## Problem

There is a class with `m` students and `n` exams. You are given a **0-indexed** `m x n` integer matrix `score`, where each row represents one student and `score[i][j]` denotes the score the `iᵗʰ` student got in the `jᵗʰ` exam. The matrix `score` contains **distinct** integers only.

You are also given an integer `k`. Sort the students (i.e., the rows of the matrix) by their scores in the `kᵗʰ` (**0-indexed**) exam from the highest to the lowest.

Return _the matrix after sorting it._

<https://leetcode.cn/problems/sort-the-students-by-their-kth-score/>

**Example 1:**

{% invert %}
![case1](assets/2545-sort-the-students-by-their-kth-score/case1.png)
{% endinvert %}

> Input: `score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2`
> Output: `[[7,5,11,2],[10,6,9,1],[4,8,3,15]]`
> Explanation: In the above diagram, S denotes the student, while E denotes the exam.
>
> - The student with index 1 scored 11 in exam 2, which is the highest score, so they got first place.
> - The student with index 0 scored 9 in exam 2, which is the second highest score, so they got second place.
> - The student with index 2 scored 3 in exam 2, which is the lowest score, so they got third place.

**Example 2:**

{% invert %}
![case2](assets/2545-sort-the-students-by-their-kth-score/case2.png)
{% endinvert %}

> Input: `score = [[3,4],[5,6]], k = 0`
> Output: `[[5,6],[3,4]]`
> Explanation: In the above diagram, S denotes the student, while E denotes the exam.
>
> - The student with index 1 scored 5 in exam 0, which is the highest score, so they got first place.
> - The student with index 0 scored 3 in exam 0, which is the lowest score, so they got second place.

**Constraints:**

- `m == score.length`
- `n == score[i].length`
- `1 <= m, n <= 250`
- `1 <= score[i][j] <= 10⁵`
- `score` consists of **distinct** integers.
- `0 <= k < n`

## Test Cases

``` python
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
```

{% asset_code coding/2545-sort-the-students-by-their-kth-score/solution_test.py %}

## Thoughts

这题用 Python 实现是不是某种程度上的「作弊」呢……

## Code

{% asset_code coding/2545-sort-the-students-by-their-kth-score/solution.py %}
