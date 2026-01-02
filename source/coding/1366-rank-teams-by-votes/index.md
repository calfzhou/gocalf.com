---
title: 1366. Rank Teams by Votes
notebook: coding
tags:
- medium
date: 2024-12-29 00:42:59
updated: 2024-12-29 00:42:59
---
## Problem

In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

You are given an array of strings `votes` which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return _a string of all teams **sorted** by the ranking system_.

<https://leetcode.cn/problems/rank-teams-by-votes/>

**Example 1:**

> Input: `votes = ["ABC","ACB","ABC","ACB","ACB"]`
> Output: `"ACB"`
> Explanation:
> Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
> Team B was ranked second by 2 voters and ranked third by 3 voters.
> Team C was ranked second by 3 voters and ranked third by 2 voters.
> As most of the voters ranked C second, team C is the second team, and team B is the third.

**Example 2:**

> Input: `votes = ["WXYZ","XYZW"]`
> Output: `"XWYZ"`
> Explanation:
> X is the winner due to the tie-breaking rule. X has the same votes as W for the first position, but X has one vote in the second position, while W does not have any votes in the second position.

**Example 3:**

> Input: `votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]`
> Output: `"ZMNAGUEDSJYLBOPHRQICWFXTVK"`
> Explanation: Only one voter, so their votes are used for the ranking.

**Constraints:**

- `1 <= votes.length <= 1000`
- `1 <= votes[i].length <= 26`
- `votes[i].length == votes[j].length` for `0 <= i, j < votes.length`.
- `votes[i][j]` is an English **uppercase** letter.
- All characters of `votes[i]` are unique.
- All the characters that occur in `votes[0]` **also occur** in `votes[j]` where `1 <= j < votes.length`.

## Test Cases

```python
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
```

{% snippet solution_test.py %}

## Thoughts

设一共有 n 个 team。给每个 team 初始化一个大小为 n 的全零数组，表示这个 team 被投在每个位置的票数。

遍历所有的 votes（设有 m 个），更新每个 team 被投在每个位置的票数。

先对所有 team 按字典序排序。再按票数数组按降序排序。第二次排序的结果就是 teams 的最终排序结果。

空间复杂度 `O(n²)`，时间复杂度 `O(m * n + n² log n)`。其中 `O(n² log n)` 是第二次排序的时间，因为每次比较都需要最环情况下 `O(n)` 次判断。

## Code

{% snippet solution.py %}
