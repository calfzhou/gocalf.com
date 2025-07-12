---
title: 1400. Construct K Palindrome Strings
notebook: coding
tags:
- medium
date: 2025-01-11 09:49:54
updated: 2025-01-11 09:49:54
---
## Problem

Given a string `s` and an integer `k`, return `true` _if you can use all the characters in_ `s` _to construct_ `k` _palindrome strings or_ `false` _otherwise_.

<https://leetcode.com/problems/construct-k-palindrome-strings/>

**Example 1:**

> Input: `s = "annabelle", k = 2`
> Output: `true`
> Explanation: You can construct two palindromes using all characters in s.
> Some possible constructions `"anna" + "elble"`, `"anbna" + "elle"`, `"anellena" + "b"`

**Example 2:**

> Input: `s = "leetcode", k = 3`
> Output: `false`
> Explanation: It is impossible to construct 3 palindromes using all the characters of s.

**Example 3:**

> Input: `s = "true", k = 4`
> Output: true
> Explanation: The only possible solution is to put each character in a separate string.

**Constraints:**

- `1 <= s.length <= 10⁵`
- `s` consists of lowercase English letters.
- `1 <= k <= 10⁵`

## Test Cases

``` python
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
```

{% asset_code coding/assets/1400-construct-k-palindrome-strings/solution_test.py %}

## Thoughts

设 s 的长度为 n，首先如果 `n < k` 就肯定不行。

然后看 s 中个数为奇数的字符，设有 m 个（`0 ≤ m ≤ n`），因为每个回文最多只能有一个字符的个数是奇数（最中间的字符），所以如果 `m > k` 就肯定不行。

把那 m 个奇数个数的字符，各取一个出来，分别先构成一个单字符回文，一共 m 个。然后看 `k - m` 的奇偶性，如果是偶数则任取 `(k - m) / 2` 对字符，打散，每个字符构成一个独立的回文。如果是奇数，则取 `floor((k - m) / 2)` 对字符，各自构成一个单字符回文，再任取一对字符构成一个长度为二的回文。这样 s 中剩下的字符一定是成对的，可以直接都给某一个已经构造出来的回文，构成一个长的回文。

## Code

{% asset_code coding/assets/1400-construct-k-palindrome-strings/solution.py %}
