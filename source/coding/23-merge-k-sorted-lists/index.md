---
title: 23. Merge k Sorted Lists
notebook: coding
tags:
- hard
date: 2024-11-14 20:59:13
updated: 2024-11-14 20:59:13
---
## Problem

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

_Merge all the linked-lists into one sorted linked-list and return it._

<https://leetcode.com/problems/merge-k-sorted-lists/>

**Example 1:**

> Input: `lists = [[1,4,5],[1,3,4],[2,6]]`
> Output: `[1,1,2,3,4,4,5,6]`
> Explanation: The linked-lists are:
>
> ```text
> [
>   1->4->5,
>   1->3->4,
>   2->6
> ]
> ```
>
> merging them into one sorted list:
> `1->1->2->3->4->4->5->6`

**Example 2:**

> Input: lists = `[]`
> Output: `[]`

**Example 3:**

> Input: lists = `[[]]`
> Output: `[]`

**Constraints:**

- `k == lists.length`
- `0 <= k <= 10⁴`
- `0 <= lists[i].length <= 500`
- `-10⁴ <= lists[i][j] <= 10⁴`
- `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` will not exceed `10⁴`.

## Test Cases

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
```

{% asset_code solution_test.py %}

## Thoughts

[21. Merge Two Sorted Lists](../21-merge-two-sorted-lists/index.md) 的进阶版。但如果直接套用，时间复杂度是 `O(k * n)`，其中 `n` 是结果链表的总长度。因为结果链表的每个节点，都需要在 k 个数中比较得到。

大量的比较是重复的，因为排头的 k 个节点，每次只会更新一个。

这是最小堆的典型使用场景。

拿 k 个链表的头节点做成大小为 k 的最小堆，堆顶就是值最小的节点。从堆顶拿到最小值，把对应链表的下一个节点替换进来，恢复堆。如果堆顶的链表已经处理完了，就按普通的 remove-min 逻辑处理，把堆的最后一个节点替换过来，然后恢复堆。

时间复杂度为 `O(n log k)`，因为结果链表中的每个节点，只需要 `O(log k)` 时间恢复堆。

关于最小堆：直接用数组存储。i 节点（`0 <= i < k`）的父节点下标为 `(i - 1) // 2`，左子节点为 `2 * i + 1`，右子节点为 `2 * i + 2`。0 节点就是堆顶。内部节点的的下标范围是 `[0, k // 2 - 1]`，叶子节点的下标范围是 `[k // 2, k)`。

## Code

{% asset_code solution.py %}
