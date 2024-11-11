---
title: 139. Word Break
notebook: coding
tags:
- medium
date: 2024-11-11 22:57:42
updated: 2024-11-11 22:57:42
katex: true
---
## Problem

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

<https://leetcode.com/problems/word-break/description/>

**Example 1:**

> Input: `s = "leetcode", wordDict = ["leet","code"]`
> Output: `true`
> Explanation: Return true because "leetcode" can be segmented as "leet code".

**Example 2:**

> Input: `s = "applepenapple", wordDict = ["apple","pen"]`
> Output: `true`
> Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
> Note that you are allowed to reuse a dictionary word.

**Example 3:**

> Input: `s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]`
> Output: `false`

**Constraints:**

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

## Test Cases

{% asset_code coding/139-word-break/solution_test.py %}

## Thoughts

设字符串 s 的长度为 n，$s_{i,j}$ 表示其中的一个子串（$1\le i\le j\le n$）。设 `wordDict` 构成的集合为 `D`。

用 $can_{i,j}$ 表示子串 $s_{i,j}$ 对应的结果，值为 `true` 或 `false`。

那么有：

$$can_{i,j}=s_{i,j}\in D\lor \exists p:(i\le p<j,can_{i,p}\land can_{p+1,j})$$

正向计算会有大量递归和重复计算，所以用动态规划算法，用二维数组保存 $can_{i,j}$ 的值，并从最小间隔的 i、j 开始。

判定 $s_{i,j}\in D$ 时，先根据 $s_{i,j}$ 的长度剪枝，即比 `wordDict` 中所有单词都短或都长的，可以直接跳过。

可以把 `wordDict` 中所有单词放在哈希表中，直接查表。设单词的平均长度为 w，那么一次查询的时间复杂度为 `O(w)`。

或者可以自行构建 trie 树，时空复杂度与用哈希表差不多（试了一版，并不比直接用 python 的 set 快）。

整体空间复杂度为 `O(n^2)`，时间复杂度为 `O(w * n^3)`，当 `w << n` 时，约等于 `O(n^3)`。

考虑到为 true 的 $can_{i,j}$ 相对会很少，可以用哈希表/哈希集合，只记录值为 true 的 `(i, j)` 对，空间复杂度会低很多。

## Code

{% asset_code coding/139-word-break/solution.py %}

## Improve

既然值为 true 的 $can_{i,j}$ 相对会很少，也就说明有大量结果为 false 的计算是无用的，需要根据题目的场景做特定的裁剪，明显不可能的 i、j 对不应该计算。

考虑把 j 固定在字符串的最右端，即 j = n。另外设 `wordDict` （集合 `D`）中单词长度的最小最大值分别是 $w_{min}$、$w_{max}$。那么：

$$
can_{i,n}=\exists w:\begin{cases}
w_{min}\le w\le w_{max}, \\
p\overset{\underset{\mathrm{def}}{}}{=}i+w-1, \\
i\le p\le n, \\
s_{i,p}\in D, \\
p=n\lor can_{p+1,n}=true
\end{cases}
$$

也就是对于子串 $s_{i,n}$，从左端开始找出所有能匹配到的单词。假设能找到一个单词 $s_{i,p}$，对应的 $can_{p+1,n}$ 亦为 true，则 $can_{i,n}$ 为 true。

上边没发挥有效作用的 trie 树，在这里可以以更快的速度从字符串 $s_{i,n}$ 的起始位置找到所有单词。比如单词表为 `["dog", "dogs"]`，利用 trie 树可以一次扫描从 `"dogsandcat"` 中找出 `"dog"` 和 `"dogs"`。

从 n 到 1 逆向遍历 i，循环一次即可。整体时间复杂度为 `O(w * n)`，其中 w 是 `wordDict` 中单词长度均值。空间复杂度为 `O(n)` 加上单词哈希表或 trie 树的大小。

优化之后的代码：

{% asset_code coding/139-word-break/solution2.py %}

Inner method test cases:

{% asset_code coding/139-word-break/solution2_inner_test.py %}
