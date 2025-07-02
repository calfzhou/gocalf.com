---
title: 206. Reverse Linked List
notebook: coding
tags:
- easy
date: 2024-11-21 19:21:49
updated: 2024-11-21 19:21:49
---
## Problem

Given the `head` of a singly linked list, reverse the list, and return _the reversed list_.

<https://leetcode.com/problems/reverse-linked-list/>

**Example 1:**

{% invert %}
![case1](assets/206-reverse-linked-list/case1.png)
{% endinvert %}

> Input: `head = [1,2,3,4,5]`
> Output: `[5,4,3,2,1]`

**Example 2:**

{% invert %}
![case2](assets/206-reverse-linked-list/case2.png)
{% endinvert %}

> Input: `head = [1,2]`
> Output: `[2,1]`

**Example 3:**

> Input: `head = []`
> Output: `[]`

**Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## Test Cases

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

{% asset_code coding/assets/206-reverse-linked-list/solution_test.py %}

## Thoughts

非递归版比递归版更简洁。

时间复杂度 `O(n)`。空间复杂度，非递归版是 `O(1)`，递归版是 `O(n)`。

## Code

### Iteratively

{% asset_code coding/assets/206-reverse-linked-list/solution.py %}

### Recursively

{% asset_code coding/assets/206-reverse-linked-list/solution_recursive.py %}
