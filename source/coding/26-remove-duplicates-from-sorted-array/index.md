---
title: 26. Remove Duplicates from Sorted Array
notebook: coding
tags:
- easy
date: 2025-02-09 12:50:47
updated: 2025-02-09 12:50:47
---
## Problem

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return _the number of unique elements in_ `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

-   Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
-   Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

```cpp
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

<https://leetcode.cn/problems/remove-duplicates-from-sorted-array/>

**Example 1:**

> Input: `nums = [1,1,2]`
> Output: `2, nums = [1,2,_]`
> Explanation: Your function should return `k = 2`, with the first two elements of `nums` being 1 and 2 respectively.
> It does not matter what you leave beyond the returned `k` (hence they are underscores).

**Example 2:**

> Input: `nums = [0,0,1,1,1,2,2,3,3,4]`
> Output: `5, nums = [0,1,2,3,4,_,_,_,_,_]`
> Explanation: Your function should return `k = 5`, with the first five elements of `nums` being 0, 1, 2, 3, and 4 respectively.
> It does not matter what you leave beyond the returned `k` (hence they are underscores).

**Constraints:**

- `1 <= nums.length <= 3 * 10⁴`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

## Test Cases

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

```

{% asset_code coding/26-remove-duplicates-from-sorted-array/solution_test.py %}

## Thoughts

用两个指针（数组下标），r 用来读取，l 用来 in-place 写入去重后的数字。

第一个元素不需要去重，所以 l 和 r 可以都从 1 开始。对于当前的 l 和 r，如果 `nums[r]` 与 `nums[r-1]` 相等，则是重复的数字，需要丢弃，否则在位置 l 写入 `nums[l]`。

时间复杂度 `O(n)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/26-remove-duplicates-from-sorted-array/solution.py %}
