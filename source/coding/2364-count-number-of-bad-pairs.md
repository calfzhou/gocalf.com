---
title: 2364. Count Number of Bad Pairs
notebook: coding
tags:
- medium
date: 2025-02-09 14:15:31
updated: 2025-02-09 14:15:31
---
## Problem

You are given a **0-indexed** integer array `nums`. A pair of indices `(i, j)` is a **bad pair** if `i < j` and `j - i != nums[j] - nums[i]`.

Return _the total number of **bad pairs** in_ `nums`.

<https://leetcode.com/problems/count-number-of-bad-pairs/>

**Example 1:**

> Input: `nums = [4,1,3,3]`
> Output: `5`
> Explanation: The pair `(0, 1)` is a bad pair since `1 - 0 != 1 - 4`.
> The pair `(0, 2)` is a bad pair since `2 - 0 != 3 - 4`, `2 != -1`.
> The pair `(0, 3)` is a bad pair since `3 - 0 != 3 - 4`, `3 != -1`.
> The pair `(1, 2)` is a bad pair since `2 - 1 != 3 - 1`, `1 != 2`.
> The pair `(2, 3)` is a bad pair since `3 - 2 != 3 - 3`, `1 != 0`.
> There are a total of 5 bad pairs, so we return 5.

**Example 2:**

> Input: `nums = [1,2,3,4,5]`
> Output: `0`
> Explanation: There are no bad pairs.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁹`

## Test Cases

``` python
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
```

{% asset_code coding/2364-count-number-of-bad-pairs/solution_test.py %}

## Thoughts

思路跟 [1014. Best Sightseeing Pair](1014-best-sightseeing-pair) 有点儿像。先把 `j - i != nums[j] - nums[i]` 改写成 `nums[i] - i != nums[j] - j`，把 i 和 j 的耦合打散。

然后为了计算不相等 pair 的数量，可以用总数减去相等的数量。

Pair 总数显然为 `n * (n - 1) / 2`。如果有 m 个位置的 `nums[i] - i` 彼此相等，那么他们贡献了 `m * (m - 1) / 2` 个相等的 pair。

用字典记录 `nums[i] - i` 的每个不同结果对应的 i 的数量，从总数中减去所有相等的 pair 数量，所得记为题目结果。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/2364-count-number-of-bad-pairs/solution.py %}
