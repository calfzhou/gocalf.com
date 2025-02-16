---
title: 1299. Replace Elements with Greatest Element on Right Side
notebook: coding
tags:
- easy
date: 2025-02-16 17:25:34
updated: 2025-02-16 17:25:34
---
## Problem

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

<https://leetcode.cn/problems/replace-elements-with-greatest-element-on-right-side/>

**Example 1:**

> Input: `arr = [17,18,5,4,6,1]`
> Output: `[18,6,6,6,1,-1]`
> Explanation:
>
> - index 0 --> the greatest element to the right of index 0 is index 1 (18).
> - index 1 --> the greatest element to the right of index 1 is index 4 (6).
> - index 2 --> the greatest element to the right of index 2 is index 4 (6).
> - index 3 --> the greatest element to the right of index 3 is index 4 (6).
> - index 4 --> the greatest element to the right of index 4 is index 5 (1).
> - index 5 --> there are no elements to the right of index 5, so we put -1.

**Example 2:**

> Input: `arr = [400]`
> Output: `[-1]`
> Explanation: There are no elements to the right of index 0.

**Constraints:**

- `1 <= arr.length <= 10⁴`
- `1 <= arr[i] <= 10⁵`

## Test Cases

``` python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
```

{% asset_code coding/1299-replace-elements-with-greatest-element-on-right-side/solution_test.py %}

## Thoughts

可以直接 in-place 修改。从右向左扫描 arr，记录见到的最大的数字，并替换到扫描到的位置。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/1299-replace-elements-with-greatest-element-on-right-side/solution.py %}
