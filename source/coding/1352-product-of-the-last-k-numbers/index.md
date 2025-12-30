---
title: 1352. Product of the Last K Numbers
notebook: coding
tags:
- medium
date: 2025-02-14 14:19:00
updated: 2025-02-14 14:19:00
---
## Problem

Design an algorithm that accepts a stream of integers and retrieves the product of the last `k` integers of the stream.

Implement the `ProductOfNumbers` class:

- `ProductOfNumbers()` Initializes the object with an empty stream.
- `void add(int num)` Appends the integer `num` to the stream.
- `int getProduct(int k)` Returns the product of the last `k` numbers in the current list. You can assume that always the current list has at least `k` numbers.

The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

<https://leetcode.com/problems/product-of-the-last-k-numbers/>

**Example 1:**

> Input
> `["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]`
> `[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]`
>
> Output
> `[null,null,null,null,null,null,20,40,0,null,32]`
>
> Explanation
>
> ```cpp
> ProductOfNumbers productOfNumbers = new ProductOfNumbers();
> productOfNumbers.add(3);        // [3]
> productOfNumbers.add(0);        // [3,0]
> productOfNumbers.add(2);        // [3,0,2]
> productOfNumbers.add(5);        // [3,0,2,5]
> productOfNumbers.add(4);        // [3,0,2,5,4]
> productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
> productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
> productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
> productOfNumbers.add(8);        // [3,0,2,5,4,8]
> productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32
> ```

**Constraints:**

- `0 <= num <= 100`
- `1 <= k <= 4 * 10⁴`
- At most `4 * 10⁴` calls will be made to `add` and `getProduct`.
- The product of the stream at any point in time will fit in a **32-bit** integer.

**Follow-up:** Can you implement **both** `GetProduct` and `Add` to work in `O(1)` time complexity instead of `O(k)` time complexity?

## Test Cases

```python
class ProductOfNumbers:

    def __init__(self):


    def add(self, num: int) -> None:


    def getProduct(self, k: int) -> int:



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
```

{% asset_code solution_test.py %}

## Thoughts

先不考虑有 0 的情况。设已经有了 n 个数字，记录下每一个前缀子数组的乘积，这样后 k 个数字之积就等于全部 n 个数字之积除以前 `n - k` 个数字之积。第 `n + 1` 个数字到来是，用已有的 n 个数字之积乘以第 `n + 1` 个数字，依然可以有所有的前缀子数组的乘积。

如果遇到 0，那么所有包含 0 的子数组的乘积均为 0，只需要重新记录这个 0 之后的数字的前缀子数组的乘积。

`__init__`、`add` 和 `getProduct` 方法的时间复杂度均为 `O(1)`，空间复杂度 `O(n)`。其中 `self._products` 记录最后一个 0 之后的数组的所有前缀子数组的乘积，其第 0 项恒为 1 表示长度为 0 的子数组的乘积，用于简化边界处理。

## Code

{% asset_code solution.py %}
