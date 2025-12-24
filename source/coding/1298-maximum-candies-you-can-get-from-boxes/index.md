---
title: 1298. Maximum Candies You Can Get from Boxes
notebook: coding
tags:
- hard
date: 2024-12-28 20:38:00
updated: 2024-12-28 20:38:00
---
## Problem

You have `n` boxes labeled from `0` to `n - 1`. You are given four arrays: `status`, `candies`, `keys`, and `containedBoxes` where:

- `status[i]` is `1` if the `iᵗʰ` box is open and `0` if the `iᵗʰ` box is closed,
- `candies[i]` is the number of candies in the `iᵗʰ` box,
- `keys[i]` is a list of the labels of the boxes you can open after opening the `iᵗʰ` box.
- `containedBoxes[i]` is a list of the boxes you found inside the `iᵗʰ` box.

You are given an integer array `initialBoxes` that contains the labels of the boxes you initially have. You can take all the candies in **any open box** and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return _the maximum number of candies you can get following the rules above_.

<https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/>

**Example 1:**

> Input: `status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]`
> Output: `16`
> Explanation: You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
> Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
> In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
> Total number of candies collected `= 7 + 4 + 5 = 16` candy.

**Example 2:**

> Input: `status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]`
> Output: `6`
> Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
> The total number of candies will be 6.

**Constraints:**

- `n == status.length == candies.length == keys.length == containedBoxes.length`
- `1 <= n <= 1000`
- `status[i]` is either `0` or `1`.
- `1 <= candies[i] <= 1000`
- `0 <= keys[i].length <= n`
- `0 <= keys[i][j] < n`
- All values of `keys[i]` are **unique**.
- `0 <= containedBoxes[i].length <= n`
- `0 <= containedBoxes[i][j] < n`
- All values of `containedBoxes[i]` are unique.
- Each box is contained in one box at most.
- `0 <= initialBoxes.length <= n`
- `0 <= initialBoxes[i] < n`

## Test Cases

``` python
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
```

{% asset_code coding/1298-maximum-candies-you-can-get-from-boxes/solution_test.py %}

## Thoughts

> 注意题目没有限制一个盒子最多对应一把钥匙，不同的其他盒子里可以都有此盒子的钥匙。

用一个队列或者栈记录当前持有且可以打开（原本就没锁，或者后来用钥匙开锁了）的盒子，同时记录持有但暂时打不开的盒子（可以用集合，或者大小为 n 的 `true/false` 数组）。

对于每一个可以打开的盒子，取走其中的糖果并计数。然后拿出所有的钥匙，给对应的盒子开锁，如果对应的盒子已经持有，就把盒子放入待处理的队列或栈。然后拿出所有的盒子，如果能打开就放入待处理的队列或栈，否则就标记已持有，等着拿到钥匙再处理。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/1298-maximum-candies-you-can-get-from-boxes/solution.py %}
