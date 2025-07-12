---
title: 2375. Construct Smallest Number From DI String
notebook: coding
tags:
- medium
date: 2025-02-18 15:49:09
updated: 2025-02-18 15:49:09
---
## Problem

You are given a **0-indexed** string `pattern` of length `n` consisting of the characters `'I'` meaning **increasing** and `'D'` meaning **decreasing**.

A **0-indexed** string `num` of length `n + 1` is created using the following conditions:

- `num` consists of the digits `'1'` to `'9'`, where each digit is used **at most** once.
- If `pattern[i] == 'I'`, then `num[i] < num[i + 1]`.
- If `pattern[i] == 'D'`, then `num[i] > num[i + 1]`.

Return _the lexicographically **smallest** possible string_ `num` _that meets the conditions._

<https://leetcode.com/problems/construct-smallest-number-from-di-string/>

**Example 1:**

> Input: `pattern = "IIIDIDDD"`
> Output: `"123549876"`
> Explanation:
> At indices 0, 1, 2, and 4 we must have that `num[i] < num[i+1]`.
> At indices 3, 5, 6, and 7 we must have that `num[i] > num[i+1]`.
> Some possible values of num are `"245639871"`, `"135749862"`, and `"123849765"`.
> It can be proven that `"123549876"` is the smallest possible num that meets the conditions.
> Note that `"123414321"` is not possible because the digit `'1'` is used more than once.

**Example 2:**

> Input: `pattern = "DDD"`
> Output: `"4321"`
> Explanation:
> Some possible values of num are `"9876"`, `"7321"`, and `"8742"`.
> It can be proven that `"4321"` is the smallest possible num that meets the conditions.

**Constraints:**

- `1 <= pattern.length <= 8`
- `pattern` consists of only the letters `'I'` and `'D'`.

## Test Cases

``` python
class Solution:
    def smallestNumber(self, pattern: str) -> str:
```

{% asset_code coding/assets/2375-construct-smallest-number-from-di-string/solution_test.py %}

## Thoughts

用类似 [1718. Construct the Lexicographically Largest Valid Sequence](1718-construct-the-lexicographically-largest-valid-sequence) 的回溯法。

首先如果 pattern 的长度为 n，那么结果数字想要最小的话应该用数字 1 到 `n + 1`（否则假设数字 k 没使用，那么把 `k + 1` 换成 k 仍然符合 pattern，继续把 `k + 2` 换成 `k + 1`……，最终还是用到 1 到 `n + 1`）。

结果数字一共有 `n + 1` 个位置，从最左边开始，对于每个位置从小到大遍历所有未被占用的数字，然后递归地处理下一个位置。最左边的位置可以从 1 试到 `n + 1`；其他位置则要先检查 pattern 中对应的前一位的值，如果是 `"I"` 则下界为前一个数字加一，如果是 `"D"` 则上界为前一个数字减一。

时间复杂度 `O(n!)`，空间复杂度 `O(n)`。

## Code

{% asset_code coding/assets/2375-construct-smallest-number-from-di-string/solution.py %}

## Faster

前边提到长度为 n 的 pattern，结果数字应该只用到数字 1 到 `n + 1`。

如果 pattern 中没有 `"D"`，显然结果数字应该为 1 到 `n + 1` 的升序排列，即 `"123...n{n+1}"`。

如果只有最后 k 位是 `"D"`，那么结果数字的前 `n - k` 位依然用从 1 开始的递增数字，而最后 `k + 1` 位把剩余的数字降序排列即可，即 `"123...{n-k}{n+1}n{n-1}...{n-k+1}"`。

如果有若干组 `"D"`，只需要对每一组的 k 个 `"D"` 所对应的 `k + 1` 个位置（加上最后一个 `"D"` 右边一个位置）按降序排列原本这些位置的数字即可。

> TODO: 更优雅的解释。

时间复杂度 `O(n)`，空间复杂度 `O(n)`。

{% asset_code coding/assets/2375-construct-smallest-number-from-di-string/solution2.py %}
