---
title: 3159. Find Occurrences of an Element in an Array
notebook: coding
tags:
- medium
date: 2024-12-27 00:33:15
updated: 2024-12-27 00:33:15
---
## Problem

You are given an integer array `nums`, an integer array `queries`, and an integer `x`.

For each `queries[i]`, you need to find the index of the `queries[i]ᵗʰ` occurrence of `x` in the `nums` array. If there are fewer than `queries[i]` occurrences of `x`, the answer should be -1 for that query.

Return an integer array `answer` containing the answers to all queries.

<https://leetcode.cn/problems/find-occurrences-of-an-element-in-an-array/>

**Example 1:**

> Input: `nums = [1,3,1,7], queries = [1,3,2,4], x = 1`
> Output: `[0,-1,2,-1]`
> Explanation:
>
> - For the 1ˢᵗ query, the first occurrence of 1 is at index 0.
> - For the 2ⁿᵈ query, there are only two occurrences of 1 in `nums`, so the answer is -1.
> - For the 3ʳᵈ query, the second occurrence of 1 is at index 2.
> - For the 4ᵗʰ query, there are only two occurrences of 1 in `nums`, so the answer is -1.

**Example 2:**

> Input: `nums = [1,2,3], queries = [10], x = 5`
> Output: `[-1]`
> Explanation:
>
> - For the 1ˢᵗ query, 5 doesn't exist in `nums`, so the answer is -1.

**Constraints:**

- `1 <= nums.length, queries.length <= 10⁵`
- `1 <= queries[i] <= 10⁵`
- `1 <= nums[i], x <= 10⁴`

## Test Cases

```python
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
```

{% asset_code coding/3159-find-occurrences-of-an-element-in-an-array/solution_test.py %}

## Thoughts

直接按题意实现即可（这不应该是 easy 么）。

在 Python 里，直接用 list comprehension 比用 `list(filter(lambda ..., nums))` 快不少。

## Code

{% asset_code coding/3159-find-occurrences-of-an-element-in-an-array/solution.py %}
