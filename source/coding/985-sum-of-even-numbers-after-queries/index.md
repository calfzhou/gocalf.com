---
title: 985. Sum of Even Numbers After Queries
notebook: coding
tags:
- medium
date: 2025-01-01 23:07:10
updated: 2025-01-01 23:07:10
---
## Problem

You are given an integer array `nums` and an array `queries` where `queries[i] = [valᵢ, indexᵢ]`.

For each query `i`, first, apply `nums[indexᵢ] = nums[indexᵢ] + valᵢ`, then print the sum of the even values of `nums`.

Return _an integer array_ `answer` _where_ `answer[i]` _is the answer to the_ `iᵗʰ` _query_.

<https://leetcode.com/problems/sum-of-even-numbers-after-queries/>

**Example 1:**

> Input: `nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]`
> Output: `[8,6,2,4]`
> Explanation: At the beginning, the array is `[1,2,3,4]`.
> After adding 1 to `nums[0]`, the array is `[2,2,3,4]`, and the sum of even values is `2 + 2 + 4 = 8`.
> After adding -3 to `nums[1]`, the array is `[2,-1,3,4]`, and the sum of even values is `2 + 4 = 6`.
> After adding -4 to `nums[0]`, the array is `[-2,-1,3,4]`, and the sum of even values is `-2 + 4 = 2`.
> After adding 2 to `nums[3]`, the array is `[-2,-1,3,6]`, and the sum of even values is `-2 + 6 = 4`.

**Example 2:**

> Input: `nums = [1], queries = [[4,0]]`
> Output: `[0]`

**Constraints:**

- `1 <= nums.length <= 10⁴`
- `-10⁴ <= nums[i] <= 10⁴`
- `1 <= queries.length <= 10⁴`
- `-10⁴ <= valᵢ <= 10⁴`
- `0 <= indexᵢ < nums.length`

## Test Cases

``` python
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
```

{% asset_code coding/985-sum-of-even-numbers-after-queries/solution_test.py %}

## Thoughts

每次 query 只会改变一个数字，可以直接基于前一次 query 时候的偶数之和，结合本次的改动进行更新，得到新的偶数之和。

初始时计算出 nums 中所有偶数之和，记为 s。

看每次 query 对指定位置的数字的改变情况，对 s 做相应的更新，共有四种可能：

- 把一个奇数 a 变为偶数 b：`s = s + b`。
- 把一个奇数 a 变为另一个奇数 b：s 保持不变。
- 把一个偶数 a 变为奇数 b：`s = s - a`。
- 把一个偶数 a 变为另一个偶数 b：`s = s - a + b`。

时间复杂度 `O(n + m)`，附加的空间复杂度 `O(1)`。其中 n 是 nums 的长度，m 是 queries 的长度。

## Code

{% asset_code coding/985-sum-of-even-numbers-after-queries/solution.py %}
