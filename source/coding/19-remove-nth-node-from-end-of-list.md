---
title: 19. Remove Nth Node From End of List
notebook: coding
tags:
- medium
date: 2024-11-14 17:47:46
updated: 2024-11-14 17:47:46
---
## Problem

Given the `head` of a linked list, remove the `n^th` node from the end of the list and return its head.

<https://leetcode.com/problems/remove-nth-node-from-end-of-list/>

**Example 1:**

{% invert %}
{% image 19-remove-nth-node-from-end-of-list/case1.png %}
{% endinvert %}

> Input: `head = [1,2,3,4,5], n = 2`
> Output: `[1,2,3,5]`

**Example 2:**

> Input: `head = [1], n = 1`
> Output: `[]`

**Example 3:**

> Input: `head = [1,2], n = 1`
> Output: `[1]`

**Constraints:**

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## Test Cases

{% asset_code coding/19-remove-nth-node-from-end-of-list/solution_test.py %}

## Thoughts

两个指针 p1、p2 都指向链表头，让 p2 先走 n 步，然后与 p1 一起往前走。每次让 p2 先走，没到的话再让 p1 走，这样当 p2 走到头的时候，p1 指向倒数第 n 个节点的前一个。

给链表前边加一个虚拟节点，指向 head，在处理边界的时候会方便很多。

## Code

{% asset_code coding/19-remove-nth-node-from-end-of-list/solution.py %}
