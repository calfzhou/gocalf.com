---
title: 21. Merge Two Sorted Lists
notebook: coding
tags:
- easy
date: 2024-11-14 18:36:57
updated: 2024-11-14 18:36:57
---
## Problem

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

<https://leetcode.com/problems/merge-two-sorted-lists/>

**Example 1:**

{% invert %}
{% image 21-merge-two-sorted-lists/case1.png %}
{% endinvert %}

> Input: `list1 = [1,2,4], list2 = [1,3,4]`
> Output: `[1,1,2,3,4,4]`

**Example 2:**

> Input: `list1 = [], list2 = []`
> Output: `[]`

**Example 3:**

> Input: `list1 = [], list2 = [0]`
> Output: `[0]`

**Constraints:**

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

## Test Cases

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
```

{% asset_code coding/21-merge-two-sorted-lists/solution_test.py %}

## Thoughts

给链表前边加一个虚拟节点，指向链表的第一个节点，在处理边界的时候会方便很多。

## Code

{% asset_code coding/21-merge-two-sorted-lists/solution.py %}
