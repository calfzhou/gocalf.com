---
title: 1982. Find Array Given Subset Sums
notebook: coding
tags:
- hard
- difficult
date: 2024-12-09 22:09:31
updated: 2024-12-09 22:09:31
---
## Problem

You are given an integer `n` representing the length of an unknown array that you are trying to recover. You are also given an array `sums` containing the values of all `2ⁿ` **subset sums** of the unknown array (in no particular order).

Return _the array_ `ans` _of length_ `n` _representing the unknown array. If **multiple** answers exist, return **any** of them_.

An array `sub` is a **subset** of an array `arr` if `sub` can be obtained from `arr` by deleting some (possibly zero or all) elements of `arr`. The sum of the elements in `sub` is one possible **subset sum** of `arr`. The sum of an empty array is considered to be `0`.

**Note:** Test cases are generated such that there will **always** be at least one correct answer.

<https://leetcode.com/problems/find-array-given-subset-sums/>

**Example 1:**

> Input: `n = 3, sums = [-3,-2,-1,0,0,1,2,3]`
> Output: `[1,2,-3]`
> Explanation: `[1,2,-3]` is able to achieve the given subset sums:
>
> - `[]`: sum is 0
> - `[1]`: sum is 1
> - `[2]`: sum is 2
> - `[1,2]`: sum is 3
> - `[-3]`: sum is -3
> - `[1,-3]`: sum is -2
> - `[2,-3]`: sum is -1
> - `[1,2,-3]`: sum is 0
>
> Note that any permutation of `[1,2,-3]` and also any permutation of `[-1,-2,3]` will also be accepted.

**Example 2:**

> Input: `n = 2, sums = [0,0,0,0]`
> Output: `[0,0]`
> Explanation: The only correct answer is `[0,0]`.

**Example 3:**

> Input: `n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]`
> Output: `[0,-1,4,5]`
> Explanation: `[0,-1,4,5]` is able to achieve the given subset sums.

**Constraints:**

- `1 <= n <= 15`
- `sums.length == 2ⁿ`
- `-10⁴ <= sums[i] <= 10⁴`

## Test Cases

``` python
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
```

{% asset_code coding/1982-find-array-given-subset-sums/solution_test.py %}

## Thoughts

> 被正负数混合的情况搞到头疼。最后发现一直徘徊在正确解法的门口却始终没能踏入第一步。

如果 `arr` 中有正数，显然 `sums` 中最大值就是所有正数之和（记为 `s1`）。它与第二大的值（记为 `s2`）之差（`d = s1 - s2 >= 0`）有三种可能，一是 `d = 0`，说明 `arr` 中有 0；二是 `d` 是最小的正数；三是 `-d` 是最大的负数。

> 实际上如果 `arr` 中没有正数也类似，那么 `s1 = 0`，要么 `d = 0` 存在于 `arr` 中，要么 `-d` 是最大的负数（少了 `d` 是正数的可能）。

先看 d 存在于 `arr`（d 是最小的正数）的情况。这时候希望能够把 `sums` 分成两半，一半由所有包含 d 在内的 subset 之和构成，另一半由所有不包含 d 的 subset 之和构成。取所有不包含 d 的 subset 之和（一共有 `len(sums) / 2` 个），就是可以按照相同逻辑递归处理的子问题。

关键在于如何拆分 `sums`。

开始的想法是先计算 `arr` 的总和（`arr_sum = sum(sums) / 2ⁿ⁻¹`），然后对于 `sums` 中的任何一个值 a，一定有 `b = arr_sum - a` 也在 `sums` 中，且 a 和 b 产生于互补的两个 subset。显然 d 属于且只属于其中的一个。看 `a - d` 和 `b - d` 哪一个不存在于 `sums`，对应的就是不含 d 的 subset 之和。

麻烦就在于，有可能 `a - d` 和 `b - d` 都存在于 `sums`，如果 `a ≠ b` 那就不能随便选。

还有个想法是看 `sums` 中任何一个值 a，如果 a 是某个包含 d 的 subset 之和，那么必然有 `a - d` 在 `nums` 中；如果 `a - d` 不存在，则 a 一定是某个不含 d 的 subset 之和。遇到同样的问题，即使 a 是某个不含 d 的 subset 之和，`a - d` 也可能存在于 `sums` 中。

做了 [954. Array of Doubled Pairs](../954-array-of-doubled-pairs/index.md) 之后发现二者要处理的问题是类似的。在 [problem 954](../954-array-of-doubled-pairs/index.md) 中需要判断 `arr` 中任意一个值 `val`，`val * 2` 或 `val / 2` 是否也在 `arr` 中，而二者可能同时存在，无法确定应该跟谁配对。解决的办法是（考虑到正负数则按绝对值）排序，按顺序检查，`val` 的两倍一定排在 `val` 之后，避免了歧义性。

借鉴这个想法，对 `sums` 按照降序排列，因为 `d >= 0`，显然对于任意的一对 `a` 和 `a - d`，`a - d` 一定排在后边。对于第一个数 a，可知 `a - d` 一定存在且排在后边，把 `a - d` 删掉，就能保证之后遇到的每个值 a，对应的 `a - d` 一定还存在且排在 a 后边。这样就可以选出来所有不含 d 的 subset 之和。

前边假设了 d 存在于 `arr` 中，这个假设不一定成立。如果 `arr` 中没有 d，而是有 `-d`，那么对于刚才遍历到的任意一对 `a` 和 `a - d`，都可以看作是 `b - (-d)` 和 `b`（其中 `b = a + (-d)`），仍然可以选出来所有不含 `-d` 的 subset 之和。

所以先不管实际存在于 `arr` 中的到底是 `d` 还是 `-d`，直接按降序遍历 `sums`，把它拆分成两个一样大的数组。任意一对 `a` 和 `a - d`，把前者放入子数组 `A`，后者放入子数组 `B`。最后看 `d` 在 `A` 中是否存在。如果 `d` 在 `A` 中存在，说明正数 `d` 存在于 `arr` 中，且 `B` 里的值都是不含 `d` 的 subset 之和。否则说明负数 `-d` 存在于 `arr` 中，且 `A` 里的值都是不含 `-d` 的 subset 之和。

> 当然也有可能 `d` 和 `-d` 同时存在于 `arr` 中，没关系，这一轮先拿到 `d`，下一轮就能识别到 `-d`（如果没有更多的 `d`）。

回过头再看，其实也可以先取 `sums` 中最小的两个值（`s1 - s2 = d <= 0`，可能是负数 `d` 也可能是正数 `-d`），然后按照升序遍历 `nums`，效果是完全一样的。

外层循环共 n 次，每次都要遍历一遍剩余的 `sums` 数组，并确定出 `arr` 中的一个值。总共时间复杂度 `O(n * 2ⁿ)`，空间复杂度 `O(2ⁿ)`。

## Code

{% asset_code coding/1982-find-array-given-subset-sums/solution.py %}
