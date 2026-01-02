---
title: 2593. Find Score of an Array After Marking All Elements
notebook: coding
tags:
- medium
date: 2024-12-13 10:03:54
updated: 2024-12-13 10:03:54
---
## Problem

You are given an array `nums` consisting of positive integers.

Starting with `score = 0`, apply the following algorithm:

- Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
- Add the value of the chosen integer to `score`.
- Mark **the chosen element and its two adjacent elements if they exist**.
- Repeat until all the array elements are marked.

Return _the score you get after applying the above algorithm_.

<https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/>

**Example 1:**

> Input: `nums = [2,1,3,4,5,2]`
> Output: `7`
> Explanation: We mark the elements as follows:
>
> - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: `[`{% u 2 %}`,`{% u 1 %}`,`{% u 3 %}`,4,5,2]`.
> - 2 is the smallest unmarked element, so we mark it and its left adjacent element: `[`{% u 2 %}`,`{% u 1 %}`,`{% u 3 %}`,4,`{% u 5 %}`,`{% u 2 %}`]`.
> - 4 is the only remaining unmarked element, so we mark it: `[`{% u 2 %}`,`{% u 1 %}`,`{% u 3 %}`,`{% u 4 %}`,`{% u 5 %}`,`{% u 2 %}`]`.
>
> Our score is `1 + 2 + 4 = 7`.

**Example 2:**

> Input: `nums = [2,3,5,1,3,2]`
> Output: `5`
> Explanation: We mark the elements as follows:
>
> - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: `[2,3,`{% u 5 %}`,`{% u 1 %}`,`{% u 3 %}`,2]`.
> - 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: `[`{% u 2 %}`,`{% u 3 %}`,`{% u 5 %}`,`{% u 1 %}`,`{% u 3 %}`,2]`.
> - 2 is the only remaining unmarked element, so we mark it: `[`{% u 2 %}`,`{% u 3 %}`,`{% u 5 %}`,`{% u 1 %}`,`{% u 3 %}`,`{% u 2 %}`]`.
>
> Our score is `1 + 2 + 2 = 5`.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁶`

## Test Cases

```python
class Solution:
    def findScore(self, nums: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

直接对 `nums` 排序。但还需要保留位置信息，可以创建一个下标数组，对其按 `nums` 值排序。另外用一个数组记录 `nums` 中哪些值被标记了。

时间 `O(n log n)`，空间 `O(n)`。

## Code

{% snippet solution.py %}
