---
title: 128. Longest Consecutive Sequence
notebook: coding
tags:
- medium
date: 2024-11-09 20:37:50
updated: 2024-11-09 20:37:50
---
## Problem

Given an unsorted array of integers `nums`, return _the length of the longest consecutive elements sequence._

You must write an algorithm that runs in `O(n)` time.

<https://leetcode.com/problems/longest-consecutive-sequence/>

**Example 1:**

> Input: nums = [100,4,200,1,3,2]
> Output: 4
> Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

**Example 2:**

> Input: nums = [0,3,7,2,5,8,4,6,0,1]
> Output: 9

**Constraints:**

- `0 <= nums.length <= 10⁵`
- `-10⁹ <= nums[i] <= 10⁹`

## Test Cases

``` python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
```

{% asset_code coding/128-longest-consecutive-sequence/solution_test.py %}

## Thoughts

开始以为是那个经典的动态规划 LCS (Longest Common Subsequence) 问题，仔细看发现不是。

限制 `O(n)` 是最大的难度。

初步考虑用散列排序。虽然 `O(10⁹) + O(n)` 依然算 `O(n)`，但实际的速度就过于慢了，内存占用也大。

需要借助哈希表，假设哈希表的查找是 `O(1)` 时间。

难点：

> 如何借助哈希表，判定 consecutive sequence 及其长度。

哈希表的 key 也是无序的。所以对 consecutive sequence 的第一个数和非第一个数要区别对待。

判定是不是第一个数，看其减一是否也在哈希表中。不是第一个数就不用管了。

如果是第一个数，不断加一，直到加出来的数不在哈希表中。

时间复杂度是 O(n)。因为每个序列的第一个数，向后检查的数字个数约等于这个序列的长度，累加起来约等于总数量。

## Code

{% asset_code coding/128-longest-consecutive-sequence/solution.py %}
