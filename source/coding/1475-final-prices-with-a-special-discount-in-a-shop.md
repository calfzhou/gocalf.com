---
title: 1475. Final Prices With a Special Discount in a Shop
notebook: coding
tags:
- easy
date: 2024-12-18 11:31:56
updated: 2024-12-18 11:31:56
---
## Problem

You are given an integer array `prices` where `prices[i]` is the price of the `iᵗʰ` item in a shop.

There is a special discount for items in the shop. If you buy the `iᵗʰ` item, then you will receive a discount equivalent to `prices[j]` where `j` is the minimum index such that `j > i` and `prices[j] <= prices[i]`. Otherwise, you will not receive any discount at all.

Return an integer array `answer` where `answer[i]` is the final price you will pay for the `ith` item of the shop, considering the special discount.

<https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/>

**Example 1:**

> Input: `prices = [8,4,6,2,3]`
> Output: `[4,2,4,2,3]`
> Explanation:
> For item 0 with `price[0]=8` you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is `8 - 4 = 4`.
> For item 1 with `price[1]=4` you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is `4 - 2 = 2`.
> For item 2 with `price[2]=6` you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is `6 - 2 = 4`.
> For items 3 and 4 you will not receive any discount at all.

**Example 2:**

> Input: `prices = [1,2,3,4,5]`
> Output: `[1,2,3,4,5]`
> Explanation: In this case, for all items, you will not receive any discount at all.

**Example 3:**

> Input: `prices = [10,1,1,6]`
> Output: `[9,0,1,6]`

**Constraints:**

- `1 <= prices.length <= 500`
- `1 <= prices[i] <= 1000`

## Test Cases

``` python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
```

{% asset_code coding/1475-final-prices-with-a-special-discount-in-a-shop/solution_test.py %}

## Thoughts

按题目限定的规模，直接暴力（brute force）就够了。对于位置 i，从 `i + 1` 开始找到第一个不高于 `prices[i]` 的价格，作为折扣减去即可。

时间复杂度 `O(n²)`，附加的空间复杂度 `O(1)`。

## Code

{% asset_code coding/1475-final-prices-with-a-special-discount-in-a-shop/solution.py %}

## O(n log n)

有点儿类似 [1847. Closest Room](1847-closest-room)，事先对 prices 排序，从小到大扫描，把不高于当前价格的商品加入到有序集合，该有序集合按商品下标保持有序。然后在该有序集合中用二分法查找当前价格的下标，找到大于其下标中的最小。

扫描排序后 prices 的过程中，所有已经处理过的就都不比当前价格高，对于重复的相等价格，可以在前边排序的时候，优先按价格，其次按下标（逆序）排序，确保可选的商品一定会被先处理。

时间复杂度 `O(n log n)`（虽然 Python list 的 [`bisect.insort`](https://docs.python.org/3/library/bisect.html#bisect.insort) 也是 `O(n)` 时间，但在当下规模下还是比较快的，更大规模可以用其他有序集合的实现），空间复杂度 `O(n)`。

不过实际提交跑就很慢，可能系数太大了。

{% asset_code coding/1475-final-prices-with-a-special-discount-in-a-shop/solution_nlogn.py %}

## O(n)

这种找左侧/右侧第一个比当前元素小/大的问题，都可以使用单调栈，线性时间可解。

单调栈是保持栈里的元素有序。

比如 `prices = [8,4,6,2,5]`。从右向左扫描 prices。

1. 第 -1 个元素 5：此时栈为空，说明没有在其右边且不大于它的元素。将 5 入栈。
2. 第 -2 个元素 2：此时栈顶为 5，大于 2，把 5 弹出。之后栈变为空，也说明没有在其右边且不大于它的元素。将 2 入栈。这里的关键是 5 的出栈是安全的，因为：
   - 如果后续元素小于 2，那么也一定小于 5，5 在这里没用；
   - 如果后续元素大于等于 2，2 就是离它最近且不大于它的元素，也不需要考虑 5。
3. 第 -3 个元素 6：此时栈顶 2 小于等于 6，说明 2 就是其右边第一个不大于它的元素，即为相应的折扣。然后将 6 入栈（目前栈为 `[2, 6]`）。
4. 第 -4 个元素 4：栈顶 6 大于 4，弹出。栈顶变为 2，小于等于 6，说明 2 就是其右边第一个不大于它的元素，即为相应的折扣。将 4 入栈（即 `[2, 4]`）。
5. 第 -5 个元素 8：栈顶 4 小于等于 8，即为相应折扣。将 8 入栈（即 `[2, 4, 8]`）。

{% asset_code coding/1475-final-prices-with-a-special-discount-in-a-shop/solution_n.py %}
