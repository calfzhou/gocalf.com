---
title: 300. Longest Increasing Subsequence
notebook: coding
tags:
- medium
- hard
date: 2024-11-17 09:19:04
updated: 2024-11-17 21:37:09
katex: true
---
## Problem

Given an integer array `nums`, return _the length of the longest **strictly increasing subsequence**_.

> A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

<https://leetcode.com/problems/longest-increasing-subsequence/description/>

**Example 1:**

> Input: `nums = [10,9,2,5,3,7,101,18]`
> Output: `4`
> Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

**Example 2:**

> Input: `nums = [0,1,0,3,2,3]`
> Output: `4`

**Example 3:**

> Input: `nums = [7,7,7,7,7,7,7]`
> Output: `1`

**Constraints:**

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## Test Cases

{% asset_code coding/300-longest-increasing-subsequence/solution_test.py %}

## Thoughts

### 正向思路

先看第一个数字（如 10），它自己可以构成一个 inc-sub (increasing subsequence)，长度为 1。

再看第二个数字（如 9），有两个选择：

1. 跟 10 组成新的 inc-sub，长度比 10 自己构成的 inc-sub 多 1。但是不满足单调递增，pass。
2. 自己成为一个独立的 inc-sub，长度为 1。

可见如果 inc-sub 以第二个数字（9）结束，长度只能是 1。

再看第三个数字（2），有三个选择：

1. 跟在 10 结尾的 inc-sub 后边——不递增，pass。
2. 跟在 9 结尾的 inc-sub 后边——不递增，pass。
3. 自己独立，长度为 1。

因此以其作为结尾的 inc-sub，长度只能是 1。

再看第四个数字（5），有四个选择：

1. 跟在 10 结尾的 inc-sub 后边——不递增，pass。
2. 跟在 9 结尾的 inc-sub 后边——不递增，pass。
3. 跟在 3 结尾的 inc-sub 后边，长度比以 3 结尾的最长的 inc-sub 多 1，为 2。
4. 自己独立，长度为 1。

可见以其作为结尾的 inc-sub，最长可以是 2。

### 动态规划

以此类推，需要记录任意的 i（`0 <= i < n`），以其作为结束的 inc-sub 的最大长度，记为 `l[i]`。注意关键点是「以其作为结束的」。

根据前边的推理可知：

$$
l[i+1]=max\{1, \forall 0\le p\le i\land nums[i+1]>nums[p]:l[p]+1\}
$$

求出所有的 `l[i]` 之后，注意 `l[n-1]` 并不是答案，这只是以 `nums[n-1]` 结束的 inc-sub 的最大长度。

题目的答案是 $max_{0\le i<n}l[i]$。

空间复杂度是 `O(n)`，时间复杂度是 `O(n^2)`。

## Code

{% asset_code coding/300-longest-increasing-subsequence/solution.py %}

## Faster - O(n log n)

这就是 hard 级别的了。

换个用例：`[6, 3, 5, 10, 11, 2, 9, 14, 13, 7, 4, 8, 12]`。

从最左边开始。第一个数字 `6`，自己可以是一个 inc-sub，长度为 1。

用一个表格来记录，表格的第几列就表示 inc-sub 的第几个元素。现在 `6` 可以放在第一列，如：

$$
\def\arraystretch{1.5}
   \begin{array}{c:c:c:c:c}
   \boxed 1 & \boxed 2 & \boxed 3 & \boxed 4 & \boxed 5 \\ \hline
   6
\end{array}
$$

第二个数字 `3`，比前边的 `6` 小，无法与 `6` 组成 inc-sub，但它可以自己开始一个新的 inc-sub。把它写在第一列刚才 `6` 的下边。

这里的关键：如果 `6` 能跟再后边的数字组成一个 inc-sub，那么把 `6` 换成 `3` 也一定还是同样长度的 inc-sub，所以就再也不用关注这个 `6` 了，在表格里打个叉标记一下（为了强调之后再也不用管这个 `6`）。现在表格如下：

$$
\def\arraystretch{1.5}
   \begin{array}{c:c:c:c:c}
   \boxed 1 & \boxed 2 & \boxed 3 & \boxed 4 & \boxed 5 \\ \hline
   \xcancel 6 \\
   \hdashline
   3
\end{array}
$$

第三个数字 `5` 比 `3` 大，可以跟在 `3` 后边组成长度为 2 的 inc-sub（虽然 `5` 比 `6` 小，但根本不用管 `6`），把 `5` 写在 `3` 同一行的第二列。再后边紧挨着的 `10` 和 `11` 也类似，挨着往后写，得到：

$$
\def\arraystretch{1.5}
   \begin{array}{c:c:c:c:c}
   \boxed 1 & \boxed 2 & \boxed 3 & \boxed 4 & \boxed 5 \\ \hline
   \xcancel 6  \\
   \hdashline
   3 & 5 & 10 & 11
\end{array}
$$

下一个是数字 `2`，比 `11`、`10`、`9` 以及 `3` 都小，不能跟在任何已有的数字后边，只能自己构成新的 inc-sub，写在第一列 `3` 的下边。

重复一次最关键的点：虽然现在 `3 - 5 - 10 - 11` 已经是长度为 4 的 inc-sub，而 `2` 自己只是长度为 1 的 inc-sub，仍然可以发现，以后都可以不用再管这个 `3` 了。

即使 `3` 能跟以后的数字组成新的更长的 inc-sub，在这个 inc-sub 中把 `3` 换成 `2` 完全没影响，而且直接基于 `2` 也一定能找到该 inc-sub。

而如果 `3` 开头的更长的 inc-sub 也还包含后边的 `5` 甚至 `10` 和 `11`，以 `11` 为例，因为它还在表格中（没被划掉），该 inc-sub 的下一个数在确定的时候只需要跟 `11` 比较大小就足够了，也跟 `3` 没关系。

因此把 `2` 写在 `3` 下边之后，可以把 `3` 也划掉，以后都可以不再关注它。

这里还有个很关键的点，也是这个算法里最违背直觉的地方：虽然把 `3` 划掉，但并不表示最长的 inc-sub 不可以以 `3` 开头。这里是要算出最长 inc-sub 的长度，并不是在记录 inc-sub 本身。划掉 `3` 并不意味着 `3` 失去了包含在最长 inc-sub 中的可能性，只是说在对后续数字做判定的时候，不需要再考虑这个 `3`。

这个算法能够更快，完全就是因为在这个表格中，每列都只需要关注最小的那一个数，所有上边的更大的数字都完全不用再管。

目前的表格如下：

$$
\def\arraystretch{1.5}
   \begin{array}{c:c:c:c:c}
   \boxed 1 & \boxed 2 & \boxed 3 & \boxed 4 & \boxed 5 \\ \hline
   \xcancel 6  \\
   \hdashline
   \xcancel 3 & 5 & 10 & 11 \\
   \hdashline
   2
\end{array}
$$

下一个数字 `9`，按照同样的思路去处理。首先它比 `11` 和 `10` 都小，不能跟在它们的后边。但它比第二列的 `5` 大，是可以跟在 `5`（以及 `5` 前边的 `3`，虽然已经划掉了）后边，有机会组成新的更长的 inc-sub。那能不能直接跟在 `2` 后边呢？可以，但一定会比跟在 `5` 后边要短。

所以把 `9` 写在第三列 `10` 的下边，同理，可以把 `10` 划掉，以后都不用再关注。于是：

$$
\def\arraystretch{1.5}
   \begin{array}{c:c:c:c:c}
   \boxed 1 & \boxed 2 & \boxed 3 & \boxed 4 & \boxed 5 \\ \hline
   \xcancel 6  \\
   \hdashline
   \xcancel 3 & 5 & \xcancel{10} & 11 \\
   \hdashline
   2 & & 9
\end{array}
$$

可以发现，已知的最长 inc-sub `3 - 5 - 10 - 11` 中已经有两个数字（`3` 和 `10`）被划掉了，但并没有任何影响，以后如果有比 `11` 大的数字，依然可以跟在 `11` 后边，组成长度为 `5` 的 inc-sub。

很巧，这样的数字来了，就是下一个数字 `14`。`14` 比第四列的 `11` 大，可以跟在后边，于是写在第五列。为了更清晰第表达出 `14` 在原始数组中是排在 `9` 之后的，把 `14` 写在 `9` 那行，而不是 `11` 那行。得到：

$$
\def\arraystretch{1.5}
   \begin{array}{c:c:c:c:c}
   \boxed 1 & \boxed 2 & \boxed 3 & \boxed 4 & \boxed 5 \\ \hline
   \xcancel 6  \\
   \hdashline
   \xcancel 3 & 5 & \xcancel{10} & 11 \\
   \hdashline
   2 & & 9 & & 14
\end{array}
$$

下一个数字 `13`，它比第五列的 `14` 小，但是比第四列的 `11` 大。类似于前边的分析可知，`13` 可以直接跟在 `11` 后边，有机会组成新的更长的 inc-sub。因此把 `13` 写在 `14` 下边，同时 `14` 可以被划掉。

$$
\def\arraystretch{1.5}
   \begin{array}{c:c:c:c:c}
   \boxed 1 & \boxed 2 & \boxed 3 & \boxed 4 & \boxed 5 \\ \hline
   \xcancel 6  \\
   \hdashline
   \xcancel 3 & 5 & \xcancel{10} & 11 \\
   \hdashline
   2 & & 9 & & \xcancel{14} \\
   \hdashline
   & & & & 13
\end{array}
$$

下一个数字 `7`，显然应该放在第三列 `9` 的下边，并划掉 `9`。为了体现 `7` 在原数组中排在 `13` 的后边，把它写在 `13` 下边一行（跟 `9` 之间空了一格）。

$$
\def\arraystretch{1.5}
   \begin{array}{c:c:c:c:c}
   \boxed 1 & \boxed 2 & \boxed 3 & \boxed 4 & \boxed 5 \\ \hline
   \xcancel 6  \\
   \hdashline
   \xcancel 3 & 5 & \xcancel{10} & 11 \\
   \hdashline
   2 & & \xcancel 9 & & \xcancel{14} \\
   \hdashline
   & & & & 13 \\
   \hdashline
   & & 7
\end{array}
$$

依次类推，把剩下的数字 `4`、`8`、`12` 也用相同的逻辑放入表格中，最终得到：

$$
\def\arraystretch{1.5}
   \begin{array}{c:c:c:c:c}
   \boxed 1 & \boxed 2 & \boxed 3 & \boxed 4 & \boxed 5 \\ \hline
   \xcancel 6  \\
   \hdashline
   \xcancel 3 & \xcancel 5 & \xcancel{10} & \xcancel{11} \\
   \hdashline
   2 & & \xcancel 9 & & \xcancel{14} \\
   \hdashline
   & & & & \xcancel{13} \\
   \hdashline
   & & 7 \\
   \hdashline
   & 4 & & 8 & 12
\end{array}
$$

再次强调，把一个数字划掉，并不代表它不会出现在 inc-sub 中，只是后续其他数字做判定的时候都不需要考虑它。

把表格中的数字连起来，就能看出来曾经识别到的 inc-sub，其中能从第一列连到最后一列的那些都是最长的 inc-sub。虽然表格中不会包含所有的 inc-sub，但最长的一定有。

连线的时候，任何一个数都只能跟它右边一列中，不高于它所在行，且高于它下边数字所在行的数字相连。

{% invert %}
{% diagramsnet 300-longest-increasing-subsequence/lic-algo.drawio %}
{% endinvert %}

从图中可以看出，数组 `[6, 3, 5, 10, 11, 2, 9, 14, 13, 7, 4, 8, 12]` 的 LIS 长度是 5，如 `3 - 5 - 10 - 11 - 14`、`3 - 5 - 10 - 11 - 13` 或 `3 - 5 - 7 - 8 - 12`（不止这些）。

算法可以加速的关键在于上边反复提到的，对于任何一列，当写入一个更小的数字时，把已有的较大数字划掉，这样所有列始终都只保留一个数字，并且这些数字是严格递增的（但并不是 inc-sub），于是可以用二分法快速判断下一个数字应该新加一列还是替换到已有的哪一列里。

总的时间复杂度是 `O(n log L)`（`L` 是 LIS 长度）最坏情况下是 `O(n log n)`。空间复杂度 `O(L)`，最坏情况 `O(n)`。

{% asset_code coding/300-longest-increasing-subsequence/solution_nlogn.py %}

其中 `buffer` 的长度始终不会超出当前处理完的原数组长度，于是可以直接利用原数组的空间，额外的空间复杂度 `O(1)`。

{% asset_code coding/300-longest-increasing-subsequence/solution_nlogn_1.py %}
