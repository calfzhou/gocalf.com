---
title: 347. Top K Frequent Elements
notebook: coding
tags:
- medium
date: 2024-11-23 17:13:07
updated: 2024-11-23 17:13:07
---
## Problem

Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.

<https://leetcode.com/problems/top-k-frequent-elements/>

**Example 1:**

> Input: `nums = [1,1,1,2,2,3], k = 2`
> Output: `[1,2]`

**Example 2:**

> Input: `nums = [1], k = 1`
> Output: `[1]`

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Test Cases

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
```

{% snippet solution_test.py %}

## Thoughts

用哈希表统计每个数字的出现次数。

然后用大小为 `k` 的最小堆，可以找到刚好第 `k` 大的词频（以及对应的数字），

设 `nums` 有 `n` 个元素，其中各不相同的数字有 `d` 个。

时间复杂度 `O(n + d log k)`，空间复杂度 `O(d)`。

小优化点：堆内元素少于 k 个时不用维护堆的结构，第 k 个元素入堆时做一次堆的构建即可。

## Code

{% snippet solution.py %}
