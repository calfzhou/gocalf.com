---
title: 638. Shopping Offers
notebook: coding
tags:
- medium
date: 2024-11-27 09:39:11
updated: 2024-11-27 09:39:11
---
## Problem

In LeetCode Store, there are `n` items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given an integer array `price` where `price[i]` is the price of the `iᵗʰ` item, and an integer array `needs` where `needs[i]` is the number of pieces of the `iᵗʰ` item you want to buy.

You are also given an array `special` where `special[i]` is of size `n + 1` where `special[i][j]` is the number of pieces of the `jᵗʰ` item in the `iᵗʰ` offer and `special[i][n]` (i.e., the last integer in the array) is the price of the `iᵗʰ` offer.

Return _the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers_. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.

<https://leetcode.cn/problems/shopping-offers/>

**Example 1:**

> Input: `price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]`
> Output: `14`
> Explanation: There are two kinds of items, A and B. Their prices are $2 and $5 respectively.
> In special offer 1, you can pay $5 for 3A and 0B
> In special offer 2, you can pay $10 for 1A and 2B.
> You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

**Example 2:**

> Input: `price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]`
> Output: `11`
> Explanation: The price of A is $2, and $3 for B, $4 for C.
> You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.
> You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C.
> You cannot add more items, though only $9 for 2A ,2B and 1C.

**Constraints:**

- `n == price.length == needs.length`
- `1 <= n <= 6`
- `0 <= price[i], needs[i] <= 10`
- `1 <= special.length <= 100`
- `special[i].length == n + 1`
- `0 <= special[i][j] <= 50`
- The input is generated that at least one of `special[i][j]` is non-zero for `0 <= j <= n - 1`.

## Test Cases

```python
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
```

{% snippet solution_test.py %}

## Thoughts

相当于 [322. Coin Change](../322-coin-change/index.md) 的进阶版，从一个币种升级成同时处理 n 个币种，目标从硬币数量最少升级为带权总和最小，除此之外没有其他本质区别。

对于任意一个需求集 `(i₁, i₂, ..., iₙ)`，要么按照每个物品的单价直接购买，要么先买下某个 special offer 然后再看剩下的部分怎么买。

同样可以事先过滤掉完全没用的 offer，比如比需要的物品种类或数量多，或者价格没有直接购买便宜。

虽然一般动态规划问题可以循环遍历所有的子问题，但现在这种有好几种物品需要购买的场景中，遍历全部需求量的组合就太低效，会有大量的计算浪费掉。所以直接用递归实现，用哈希表或者 Python 自带的缓存功能避免重复计算。

记 `k` 为 special offers 的数量，`m` 是 `needs` 中的最大值，时间复杂度为 `O(mⁿ * k * n)`，空间复杂度为 `O(mⁿ * n)`。

## Code

{% snippet solution.py %}
