---
title: 843. Guess the Word
notebook: coding
tags:
- hard
date: 2024-12-29 22:55:31
updated: 2024-12-29 22:55:31
---
## Problem

You are given an array of unique strings `words` where `words[i]` is six letters long. One word of `words` was chosen as a secret word.

You are also given the helper object `Master`. You may call `Master.guess(word)` where `word` is a six-letter-long string, and it must be from `words`. `Master.guess(word)` returns:

- `-1` if `word` is not from `words`, or
- an integer representing the number of exact matches (value and position) of your guess to the secret word.

There is a parameter `allowedGuesses` for each test case where `allowedGuesses` is the maximum number of times you can call `Master.guess(word)`.

For each test case, you should call `Master.guess` with the secret word without exceeding the maximum number of allowed guesses. You will get:

- **`"Either you took too many guesses, or you did not find the secret word."`** if you called `Master.guess` more than `allowedGuesses` times or if you did not call `Master.guess` with the secret word, or
- **`"You guessed the secret word correctly."`** if you called `Master.guess` with the secret word with the number of calls to `Master.guess` less than or equal to `allowedGuesses`.

The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the bruteforce method).

<https://leetcode.com/problems/guess-the-word/>

**Example 1:**

> Input: `secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10`
> Output: `You guessed the secret word correctly.`
> Explanation:
> `master.guess("aaaaaa")` returns -1, because `"aaaaaa"` is not in wordlist.
> `master.guess("acckzz")` returns 6, because `"acckzz"` is secret and has all 6 matches.
> `master.guess("ccbazz")` returns 3, because `"ccbazz"` has 3 matches.
> `master.guess("eiowzz")` returns 2, because `"eiowzz"` has 2 matches.
> `master.guess("abcczz")` returns 4, because `"abcczz"` has 4 matches.
> We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.

**Example 2:**

> Input: `secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10`
> Output: `You guessed the secret word correctly.`
> Explanation: Since there are two words, you can guess both.

**Constraints:**

- `1 <= words.length <= 100`
- `words[i].length == 6`
- `words[i]` consist of lowercase English letters.
- All the strings of `wordlist` are **unique**.
- `secret` exists in `words`.
- `10 <= allowedGuesses <= 30`

## Test Cases

```python
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
```

{% snippet solution_test.py %}

## Thoughts

设拿一个单词 word 调用 `Master.guess` 返回结果为 m。显然如果 `m = 6` 就猜对了，可以停止。否则有 `0 ≤ m ≤ 5`。

因为 secret 跟 word 的匹配度（the number of exact matches）为 m，那么 words 中所有跟 word 匹配度不为 m 的单词，一定不可能是 secret，可以排除掉。想要猜的最快，就要尽可能多地排除掉候选单词。

事先计算任意两个单词之间的匹配度。对于某个单词，看每个匹配度能匹配到的单词数量，取最大值，即为猜测这个单词之后，剩余候选单词数量的上限。对所有的候选单词，取剩余候选单词数量上限最小的那个进行猜测。

时间复杂度为 `O(k * n²)`，空间复杂度 `O(n²)`，其中 k 是猜测次数，根据题目限制可以认为是常数。

## Code

{% snippet solution.py %}

## Faster but May Fail

因为上边虽然每次都选剩余候选单词数量上限最小的单词，但根据猜测结果筛选之后，实际剩余的候选单词数量可能会多很多，那不如直接随机选择。

每次随机挑一个候选单词去猜测，然后删掉匹配度不一致的其他候选词。时间复杂度是 `O(k * n)`，空间复杂度 `O(n)`。但是猜测的数量就不太稳定，有时候提交后测试会失败（猜测数量达到上限）。

{% snippet solution2.py %}
