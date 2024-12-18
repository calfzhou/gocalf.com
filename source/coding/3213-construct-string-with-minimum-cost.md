---
title: 3213. Construct String with Minimum Cost
notebook: coding
tags:
- hard
date: 2024-12-17 21:39:12
updated: 2024-12-17 23:48:27
references:
- '[Aho-Corasick Algorithm in Python - GeeksforGeeks](https://www.geeksforgeeks.org/aho-corasick-algorithm-in-python/)'
---
## Problem

You are given a string `target`, an array of strings `words`, and an integer array `costs`, both arrays of the same length.

Imagine an empty string `s`.

You can perform the following operation any number of times (including **zero**):

- Choose an index `i` in the range `[0, words.length - 1]`.
- Append `words[i]` to `s`.
- The cost of operation is `costs[i]`.

Return the **minimum** cost to make `s` equal to `target`. If it's not possible, return `-1`.

<https://leetcode.cn/problems/construct-string-with-minimum-cost/>

**Example 1:**

> Input: `target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]`
> Output: `7`
> Explanation:
> The minimum cost can be achieved by performing the following operations:
>
> - Select index 1 and append `"abc"` to s at a cost of 1, resulting in s = `"abc"`.
> - Select index 2 and append `"d"` to s at a cost of 1, resulting in s = `"abcd"`.
> - Select index 4 and append `"ef"` to s at a cost of 5, resulting in s = `"abcdef"`.

**Example 2:**

> Input: `target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]`
> Output: `-1`
> Explanation:
> It is impossible to make s equal to target, so we return -1.

**Constraints:**

- `1 <= target.length <= 5 * 10⁴`
- `1 <= words.length == costs.length <= 5 * 10⁴`
- `1 <= words[i].length <= target.length`
- The total sum of `words[i].length` is less than or equal to `5 * 10⁴`.
- `target` and `words[i]` consist only of lowercase English letters.
- `1 <= costs[i] <= 10⁴`

## Test Cases

``` python
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
```

{% asset_code coding/3213-construct-string-with-minimum-cost/solution_test.py %}

## Thoughts

注意题目没有限制 words 中的单词各不相同，如果遇到重复的，需要只保留 cost 最小的那个。

### Too Slow

先尝试直观但是很慢的方法。

看以位置 i 开头的子字符串 `target[i:]`，记 `dp(i)` 表示该子问题的最小 cost。从位置 i 开始能够在 `words` 中匹配到哪些单词，设 `target[i:j]` 是 words 中的一个单词，那么 `dp(i) = min{cost(target[i:j]) + dp(j)}`。

用 words 和 costs 构建前缀树（参见 [208. Implement Trie (Prefix Tree)](208-implement-trie-prefix-tree)），把单词的 cost 记录在词尾节点上。加一个 lookup 方法（类似于 [139. Word Break](139-word-break#Improve)），找出 `target[i:]` 中以位置 i 开头所有可以匹配到的单词。

设 target 的长度为 n，单词数量为 m，单词平均长度 k（本题的 k、m、n 量级相当）。时间复杂度是 `O(mk + n²)`，空间复杂度 `O(mk + n)`。

太慢了，无法 AC，仅当练习 trie 了。

[solution_trie.py](3213-construct-string-with-minimum-cost/solution_trie.py)

实际上还可以定义 `dp'(i)` 表示子字符串 `target[:i]` 的最小 cost。并为了方便，定义 `dp'(0) = 0`，其他值均初始化为 ∞，最终所求结果为 `dp'(n)`。

令 i 从 0 递增到 `n - 1`。对于当前的 i，如果 `dp'(i) = ∞`，说明 `target[:i]` 无法由 words 中的单词拼接而成。否则看从位置 i 开始可以匹配到哪些单词，比如 `target[i:j]` 是一个单词，那么 `dp'(j) = min{dp'(j), dp'(i) + cost(target[i:j])}`。Trie 相关的代码不变，只是递推的部分变为：

``` python
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(n):
    if dp[i] < 0: continue
    for j, cost in trie_lookup(i):
        if dp[j] < 0 or dp[j] > dp[i] + cost:
            dp[j] = dp[i] + cost

return dp[n]
```

### AC Algorithm

上边直接利用 trie 树，慢在对于每一个 `target[i:]`，都要去 trie 树中进行搜索。这就很像在一个字符串中查找另一个字符串，暴力查找需要的时间是两个字符串长度之积，但用 KMP 算法（[Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)）则时间为两个字符串长度之和。这里是一个字符串和另外若干个字符串的匹配（多模式匹配？），AC 自动机（[Aho–Corasick algorithm](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm)）比较适合。

利用 AC 自动机，可以用平均 `O(mk + n)` 时间找出 target 中所有能匹配到的单词。AC 自动机的实现细节跳过。

让 AC 自动机按照从前到后的顺序返回 target 中所有能匹配到的单词，对于每个匹配，可以知道匹配区域的起止下标，以及对应单词的 cost，剩下的事情就跟上边的 `dp'` 完全一致。

整体的时间复杂度为 `O(mk + n)`，空间复杂度为 `O(mk + n)`。

## Code

{% asset_code coding/3213-construct-string-with-minimum-cost/solution.py %}

附：针对 AC 自动机的构建和多模式匹配的 test cases：

{% asset_code coding/3213-construct-string-with-minimum-cost/solution_ac_test.py %}
