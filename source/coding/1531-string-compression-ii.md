---
title: 1531. String Compression II
notebook: coding
tags:
- hard
- difficult
date: 2024-12-01 15:13:27
updated: 2024-12-01 19:57:32
katex: true
---
## Problem

[Run-length encoding](http://en.wikipedia.org/wiki/Run-length_encoding) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string `"aabccc"` we replace `"aa"` by `"a2"` and replace `"ccc"` by `"c3"`. Thus the compressed string becomes `"a2bc3"`.

Notice that in this problem, we are not adding `'1'` after single characters.

Given a string `s` and an integer `k`. You need to delete **at most** `k` characters from `s` such that the run-length encoded version of `s` has minimum length.

Find the _minimum length of the run-length encoded version of_ `s` _after deleting at most_ `k` _characters_.

<https://leetcode.com/problems/string-compression-ii/>

**Example 1:**

> Input: `s = "aaabcccd", k = 2`
> Output: `4`
> Explanation: Compressing `s` without deleting anything will give us `"a3bc3d"` of length 6. Deleting any of the characters `'a'` or `'c'` would at most decrease the length of the compressed string to 5, for instance delete 2 `'a'` then we will have `s = "abcccd"` which compressed is `abc3d`. Therefore, the optimal way is to delete `'b'` and `'d'`, then the compressed version of s will be `"a3c3"` of length 4.

**Example 2:**

> Input: `s = "aabbaa", k = 2`
> Output: `2`
> Explanation: If we delete both `'b'` characters, the resulting compressed string would be `"a4"` of length 2.

**Example 3:**

> Input: `s = "aaaaaaaaaaa", k = 0`
> Output: `3`
> Explanation: Since `k` is zero, we cannot delete anything. The compressed string is `"a11"` of length 3.

**Constraints:**

- `1 <= s.length <= 100`
- `0 <= k <= s.length`
- `s` contains only lowercase English letters.

## Test Cases

``` python
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
```

{% asset_code coding/assets/1531-string-compression-ii/solution_test.py %}

## Thoughts

RLE (Run-length encoding) 的计算逻辑在 [443. String Compression](443-string-compression) 中有，可以拿过来按照需要微调一下，计算出压缩后每个字符及其个数，以及压缩后的字符串长度。

定义函数 `clen(n)` 表示连续 `n` 个相同字符压缩后的长度，易得：

``` python
clen = lambda n: n if n < 2 else int(log10(n)) + 2
```

由于被删除字符左右两边的相同字符可以合并，带来了很多麻烦。

### Failed

本来有个想法，是统计出所有不超过 `k` 的连续字符删除的可能性，每种可能可以计算需要删掉多少个（`dc`）字符，会导致重新压缩后的长度减少多少（`dl`）。然后找性价比最高的（即 `dl - dc` 最大的，如有相同的则取 `dc` 最大的）。

对于某个字符，假设有连续 `cnt` 个，则压缩后的长度为 `clen(cnt)`。可以枚举出，压缩后的长度每要减少一，需要删掉多少个字符：

``` python
def shorten(cnt: int) -> Generator[int, None, None]:
    """Yields the number of chars to be deleted to shorten compressed length by 1, down to 0."""
    k = 0
    shorter = 10 ** int(log10(cnt)) - 1
    while shorter > 0:
        k += cnt - shorter
        yield k
        cnt = shorter
        shorter //= 10

    if cnt > 1:
        k += cnt - 1
        yield k

    yield k + 1
```

对于某个字符 `c`，在扫描字符串（或压缩结果）时，可以记录每个连续片段出现的位置。然后对于任意两个片段，计算需要删掉多少个字符（两个片段之间的全部），以及两个片段合并之后总共会减少多少压缩编码长度。

这样总共需要 `O(n²)` 时间计算出所有的删除可能性。

本想将所有的可能性放入优先队列，每次 pop 出来性价比最高的。重复操作直到 `k` 被用尽。

但是如果真的发生合并，原先计算的删除可能性中，会有一部分就失效了。如何有效地清理和更新这些失效的部分就没有很好的办法。或者就对删除之后的新字符串重新做一遍删除方案的整理。

### DP

还是按普通动态规划的思路做。

定义状态值 `dp(i, d)` 表示长度为 `i` 的子串（即 `s[0:i]`）中，删除不超过 `d` 个字符，压缩之后的最短长度。所有值初始化为 ∞ 或者足够大的数（比如 `s` 的长度即可），而 `dp(0, 0) = 0` 因为空字符串也不做删除，压缩后也是空字符串。

显然题目所求结果即为 `dp(n, k)`。

当 `dp(0, *)` 到 `dp(i-1, *)` 都已经处理好了，看如何计算 `dp(i, *)`。

先不考虑同一字符前后两个片段合并的情况。

1. 可以把第 `i` 个字符（即 `sᵢ = s[i-1]`）删掉（仅当 `d > 0` 时），那么 `dp(i, d) = dp(i-1, d-1)`。
2. 也可以不删第 `i` 个字符，但这时候需要按照压缩逻辑处理第 `i` 个字符。
   1. 如果 `sᵢ₋₁ ≠ sᵢ`，显然只需要在 `s[0:i-1]` 的压缩结果后边添加 `sᵢ` 就是新的压缩结果，可知 `dp(i, d) = dp(i-1, d) + clen(1)`。
   2. 如果 `sᵢ₋₁ = sᵢ`，需要把 `sᵢ` 和前边紧邻的相同字符压缩在一起。不妨设 `1 <= j < i`，从 `sⱼ` 到 `sᵢ` 都是同一个字符（共 `cnt = i - j + 1` 个），需要将 `sⱼ...sᵢ` 压缩成 `sᵢ{cnt}` 并添加到 `s₁...sⱼ₋₁` 的压缩结果后边。所以 `dp(i, d) = dp(j-1, d) + clen(cnt)`。
   3. 2.1 可以看作是 2.2 的特例，即 `j = i`，`cnt = 1`。

所以有：

$$
dp(i,d)=\min\begin{cases}
  dp(i-1,d-1) & \text{, }d>0 \\
  dp(j-1,d)+clen(i-j+1) & \text{, }s_{j-1}\ne s_i,\forall j\le p\le i,s_p=s_i
\end{cases}
$$

再考虑合并的场景。实际上只需要考虑 `sᵢ` 这个字符的分段合并，因为其他字符的分段合并在 `dp(0, *)` 到 `dp(i-1, *)` 中处理过了。

如果不删除第 `i` 个字符，可以从 `sᵢ` 往左，分别删除 0 个、1 个、……、d 个与 `sᵢ` 不同的字符，记录分别能够得到的连续的 `sᵢ` 的字符数。设 `0 <= r <= d`，删掉 `r` 个非 `sᵢ` 字符后，能得到 `cntᵣ` 个连续的 `sᵢ` 字符，那么 `dp(i, d) = dp(i - cntᵣ - r, d - r) + clen(cntᵣ)`。而上边的 `dp(i, d) = dp(j-1, d) + clen(cnt)` 相当于 `r = 0`。

所以最终 `dp` 的递推公式为：

$$
dp(i,d)=\min_{0\le r\le d}\begin{cases}
  dp(i-1,d-1) & \text{, }d>0 \\
  dp(i-cnt_r-r,d-r)+clen(cnt_r)
\end{cases}
$$

需要对 `1 <= i <= n`、`0 <= d <= k` 和 `0 <= r <= d` 循环遍历，但是注意 `0 <= r <= d` 并不意味着只循环 `d` 次，因为还需要确定 `cntᵣ`，最坏情况需要循环 `i` 次。总的时间复杂度为 `O(n² * k)`，空间复杂度为 `O(n * k)`。

## Code

{% asset_code coding/assets/1531-string-compression-ii/solution.py %}

## Wrong Greedy

尝试实现了前边提到的贪心策略。不再用优先队列，而是每次都重算性价比最高的删除方案。时间复杂度也是 `O(n² * k)`（或者 `O(m² * k)`，`m` 是字符的片段数）。

可惜贪心是错误的，比如 `s = "aabcccbcaabbbbcbcb", k = 8`。`s` 的长度为 `11`，直接压缩得到 `"a2bc3bca2b4cbcb"`。删除 8 个字符，最优方案是剩下 7 个 `b`，即 `b7`，压缩长度为 `2`。

但是用贪心策略可能会得到 `"a4b5"` 或者 `"cb6"`（取决于相同收益下优先取哪个方案），压缩长度是 `4` 或 `3`，都不是最优的。

{% box 错误的贪心法 color:red %}
[solution_wrong.py](1531-string-compression-ii/solution_wrong.py)
{% endbox %}
