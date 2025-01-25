---
title: 2948. Make Lexicographically Smallest Array by Swapping Elements
notebook: coding
tags:
- medium
date: 2025-01-26 00:08:10
updated: 2025-01-26 00:08:10
---
## Problem

You are given a **0-indexed** array of **positive** integers `nums` and a **positive** integer `limit`.

In one operation, you can choose any two indices `i` and `j` and swap `nums[i]` and `nums[j]` **if** `|nums[i] - nums[j]| <= limit`.

Return _the **lexicographically smallest array** that can be obtained by performing the operation any number of times_.

An array `a` is lexicographically smaller than an array `b` if in the first position where `a` and `b` differ, array `a` has an element that is less than the corresponding element in `b`. For example, the array `[2,10,3]` is lexicographically smaller than the array `[10,2,3]` because they differ at index `0` and `2 < 10`.

<https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/>

**Example 1:**

> Input: `nums = [1,5,3,9,8], limit = 2`
> Output: `[1,3,5,8,9]`
> Explanation: Apply the operation 2 times:
>
> - Swap `nums[1]` with `nums[2]`. The array becomes `[1,3,5,9,8]`
> - Swap `nums[3]` with `nums[4]`. The array becomes `[1,3,5,8,9]`
>
> We cannot obtain a lexicographically smaller array by applying any more operations.
> Note that it may be possible to get the same result by doing different operations.

**Example 2:**

> Input: `nums = [1,7,6,18,2,1], limit = 3`
> Output: `[1,6,7,18,1,2]`
> Explanation: Apply the operation 3 times:
>
> - Swap `nums[1]` with `nums[2]`. The array becomes `[1,6,7,18,2,1]`
> - Swap `nums[0]` with `nums[4]`. The array becomes `[2,6,7,18,1,1]`
> - Swap `nums[0]` with `nums[5]`. The array becomes `[1,6,7,18,1,2]`
>
> We cannot obtain a lexicographically smaller array by applying any more operations.

**Example 3:**

> Input: `nums = [1,7,28,19,10], limit = 3`
> Output: `[1,7,28,19,10]`
> Explanation: `[1,7,28,19,10]` is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁹`
- `1 <= limit <= 10⁹`

## Test Cases

``` python
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
```

{% asset_code coding/2948-make-lexicographically-smallest-array-by-swapping-elements/solution_test.py %}

## Thoughts

"Lexicographically smallest" 本质上就是要排序。但不是所有的数共同参与排序，需要考虑 limit 的限制。首先看哪些数字可以在一起做排序。

对于一组数字，如果排序之后任意相邻的两个数字之差（的绝对值，后略）都小于等于 limit，那么这一组数字就是可以一起排序的。不妨设这组数字为 `a₁ ≤ a₂ ≤ ... ≤ aₘ₋₁ ≤ aₘ`，其中任意的 `1 ≤ i < m` 满足 `aᵢ₊₁ - aᵢ ≤ limit`。

用数学归纳法很容易证明，这一组数字，不管初始顺序如何，一定能够在题目限制的交换要求下完成排序。首先如果 `m = 2`，显然可以。设 `m = k` 时也可以，那么当 `m = k + 1` 时，可以先通过交换的方式把 `a₁, a₂, ..., aₖ` 排序，如果 `aₖ₊₁` 本来就排在 `aₖ` 后边，则已经完全有序了；否则先交换 `aₖ` 和 `aₖ₊₁`，然后重新对 `a₁, a₂, ..., aₖ` 排序，同样可以完成对所有数字的排序。

于是可以先对 nums 整体排序，不妨设排序后的数组为 `sorted_nums`。从小到大遍历 `sorted_nums`，如果前后相邻两个数字之差小于等于 limit，就是同一组的，否则就不是同一组。显然同一组的数字在 `sorted_nums` 中一定是前后相连的。

分组之后，只需要在 nums 中对每个组做原地排序即可。因为 `sorted_nums` 中已经有每个组排序的结果，可以直接使用。遍历 nums，对于每个数字，可以知道其所属的组以及该位置是这一组占用的所有位置中的第几个，通过 `sorted_nums` 可以知道这一组数字排序后，这个位置应该放哪个数字。

时间复杂度 `O(n log n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/2948-make-lexicographically-smallest-array-by-swapping-elements/solution.py %}
