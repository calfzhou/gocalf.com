---
title: 1346. Check If N and Its Double Exist
notebook: coding
tags:
- easy
date: 2024-12-01 09:38:41
updated: 2024-12-01 09:38:41
---
## Problem

Given an array `arr` of integers, check if there exist two indices `i` and `j` such that :

- `i != j`
- `0 <= i, j < arr.length`
- `arr[i] == 2 * arr[j]`

<https://leetcode.com/problems/check-if-n-and-its-double-exist/>

**Example 1:**

> Input: `arr = [10,2,5,3]`
> Output: `true`
> Explanation: For `i = 0` and `j = 2`, `arr[i] == 10 == 2 * 5 == 2 * arr[j]`

**Example 2:**

> Input: `arr = [3,1,7,11]`
> Output: `false`
> Explanation: There is no i and j that satisfy the conditions.

**Constraints:**

- `2 <= arr.length <= 500`
- `-10³ <= arr[i] <= 10³`

## Test Cases

``` python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
```

{% asset_code coding/1346-check-if-n-and-its-double-exist/solution_test.py %}

## Thoughts

把所有数字放进集合，然后遍历所有的偶数，如果它的一半在集合中，则结果为真。

但是 `0` 比较特殊，`0` 除以二或者乘以二都还是 `0`，但去分不出来是不是同一个数组下标的 `0`。

可以在创建集合的时候，顺便检查数组中 `0` 的个数，如果超过一个则结果为真。

也可以一遍创建集合一边创建集合一遍就进行检查。但为了没有遗漏，就要同时检查下一个数的一半（限偶数）和两倍是否在集合中。这样能够自适应 `0`。

## Code

{% asset_code coding/1346-check-if-n-and-its-double-exist/solution.py %}

{% asset_code coding/1346-check-if-n-and-its-double-exist/solution2.py %}
