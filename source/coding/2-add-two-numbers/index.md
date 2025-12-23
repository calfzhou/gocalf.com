---
title: 2. Add Two Numbers
notebook: coding
tags:
- medium
date: 2024-12-09 11:01:20
updated: 2024-12-09 11:01:20
---
## Problem

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

<https://leetcode.com/problems/add-two-numbers/>

**Example 1:**

{% invert %}
![case1](case1.png)
{% endinvert %}

> Input: `l1 = [2,4,3], l2 = [5,6,4]`
> Output: `[7,0,8]`
> Explanation: `342 + 465 = 807`.

**Example 2:**

> Input: `l1 = [0], l2 = [0]`
> Output: `[0]`

**Example 3:**

> Input: `l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]`
> Output: `[8,9,9,9,0,0,0,1]`

**Constraints:**

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Test Cases

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
```

{% asset_code coding/2-add-two-numbers/solution_test.py %}

## Thoughts

直接同步扫描 l1 和 l2，每对节点的数字相加，结果的个位数添加到结果链表的末尾，十位数（进位）留着跟下一对节点的数字一起求和。

用一个虚拟的 head 节点可以简化边界处理。最后返回 `head.next`。另外 l1 和 l2 都扫描完之后，最后的进位如果有，也要加到结果链表末尾。

## Code

{% asset_code coding/2-add-two-numbers/solution.py %}
