---
title: 769. Max Chunks To Make Sorted
notebook: coding
tags:
- medium
date: 2024-12-19 10:10:50
updated: 2024-12-19 10:10:50
---
## Problem

You are given an integer array `arr` of length `n` that represents a permutation of the integers in the range `[0, n - 1]`.

We split `arr` into some number of **chunks** (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return _the largest number of chunks we can make to sort the array_.

<https://leetcode.com/problems/max-chunks-to-make-sorted/>

**Example 1:**

> Input: `arr = [4,3,2,1,0]`
> Output: `1`
> Explanation:
> Splitting into two or more chunks will not return the required result.
> For example, splitting into `[4, 3]`, `[2, 1, 0]` will result in `[3, 4, 0, 1, 2]`, which isn't sorted.

**Example 2:**

> Input: arr = [1,0,2,3,4]
> Output: 4
> Explanation:
> We can split into two chunks, such as `[1, 0]`, `[2, 3, 4]`.
> However, splitting into `[1, 0]`, `[2]`, `[3]`, `[4]` is the highest number of chunks possible.

**Constraints:**

- `n == arr.length`
- `1 <= n <= 10`
- `0 <= arr[i] < n`
- All the elements of `arr` are **unique**.

## Test Cases

``` python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
```

{% asset_code coding/assets/769-max-chunks-to-make-sorted/solution_test.py %}

## Thoughts

设 `arr[:i]` 已经是一个（或若干个） chunks，即 `arr[:i]` 刚好包含 0 到 `i - 1` 这 i 个数字。

从位置 i 开始找最短的 chunk。一个chunk 的特点是其下标区间与元素值区间相等。显然从 i 开始，下标区间下界就是 i，而元素值区间的下界也是 i（因为 `arr[:i]` 是 chunk）。对于从 i 到 j 的下标区间（i 和 j 都包含），上界是 j，如果 `max{arr[i:j+1]} = j`（即元素值区间的上界是 j），则 `arr[i:j+1]` 是一个区间。所以从 i 开始遇到的第一个满足条件的 j 就可以构成一个最短的 chunk。

## Code

{% asset_code coding/assets/769-max-chunks-to-make-sorted/solution.py %}
