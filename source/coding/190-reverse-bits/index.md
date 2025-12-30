---
title: 190. Reverse Bits
notebook: coding
tags:
- easy
date: 2024-11-19 15:57:07
updated: 2024-11-19 15:57:07
katex: true
---
## Problem

Reverse bits of a given 32 bits unsigned integer.

**Note:**

- Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using [2's complement notation](https://en.wikipedia.org/wiki/Two%27s_complement). Therefore, in **Example 2** above, the input represents the signed integer `-3` and the output represents the signed integer `-1073741825`.

<https://leetcode.com/problems/reverse-bits/>

**Example 1:**

> Input: `n = 00000010100101000001111010011100`
> Output: `964176192 (00111001011110000010100101000000)`
> Explanation: The input binary string `00000010100101000001111010011100` represents the unsigned integer 43261596, so return 964176192 which its binary representation is `00111001011110000010100101000000`.

**Example 2:**

> Input: `n = 11111111111111111111111111111101`
> Output: `3221225471 (10111111111111111111111111111111)`
> Explanation: The input binary string `11111111111111111111111111111101` represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is `10111111111111111111111111111111`.

**Constraints:**

- The input must be a **binary string** of length `32`

**Follow up:** If this function is called many times, how would you optimize it?

## Test Cases

{% asset_code solution_test.py %}

## Thoughts

以 8 bits 二进制数举例简化书写。

每次处理对称的一对高位和低位，如第 2 和 6 位（最低位是 1），做一个 mask，只在要处理的两位是 `1`，其他位均为 `0`，如 `0100 0010`。拿数字与 mask 做 bit-and 操作，如果结果位 0 或者等于 mask，说明数字的这两位相同，不需要处理。否则要交换这两位的数字，可以直接拿数字与 mask 做 bit-xor 即可完成交换。

## Code

```python
class Solution:
    def reverseBits(self, n: int) -> int:
```

{% asset_code solution.py %}

## Faster

二进制问题往往可以试试更「二进制」的计算方式，尽量减少计算次数。

一个 8 bits 二进制数，可以按照如下 3 次交换操作完成所有位的 reverse（注意二进制数的高位和低位可以同时做类似的计算）：

$$
\begin{matrix}
\underlinesegment{8}\space\underlinesegment{7} & \underlinesegment{6}\space\underlinesegment{5} & \underlinesegment{4}\space\underlinesegment{3} & \underlinesegment{2}\space\underlinesegment{1} \\
\leftrightarrows & \leftrightarrows & \leftrightarrows & \leftrightarrows \\
\underlinesegment{7}\space\underlinesegment{8} & \underlinesegment{5}\space\underlinesegment{6} & \underlinesegment{3}\space\underlinesegment{4} & \underlinesegment{1}\space\underlinesegment{2} \\
\end{matrix}
$$

> 把 8、6、4、2 位取出来（和 `10101010` 取 bit-and）右移一位，再把 7、5、3、1 位取出来（和 `01010101` 取 bit-and）左移一位，二者合并（bit-or）即可：
> `((n & 0xaa) >> 1) | ((n & 0x55) << 1)`

$$
\begin{matrix}
\underlinesegment{7\space 8}\space\underlinesegment{5\space 6} & \underlinesegment{3\space 4}\space\underlinesegment{1\space 2} \\
\leftrightarrows & \leftrightarrows \\
\underlinesegment{5\space 6}\space\underlinesegment{7\space 8} & \underlinesegment{1\space 2}\space\underlinesegment{3\space 4} \\
\end{matrix}
$$

> 把 8、7、4、3 位取出来右移两位，6、5、2、1 位取出来左移两位，合并：
> `((n & 0xcc) >> 2) | ((n & 0x33) << 2)`

$$
\begin{matrix}
\underlinesegment{5\space 6\space 7\space 8}\space\underlinesegment{1\space 2\space 3\space 4} \\
\leftrightarrows \\
\underlinesegment{1\space 2\space 3\space 4}\space\underlinesegment{5\space 6\space 7\space 8} \\
\end{matrix}
$$

> 把 8、7、6、5 位取出来右移四位，4、3、2、1 位取出来左移四位，合并：
> `((n & 0xf0) >> 4) | ((n & 0x0f) << 4)`

继续拓展到 32 bits，只需要做 `log 32 = 5` 次类似的操作，每次操作都有 2 次 bit-and、2 次位移和一次 bit-or 共 5 次位运算。总计 25 次位运算即可。

而之前普通循环的方法需要大约 `16 * 7 = 112` 次运算，还不包括循环控制之类的操作。

{% asset_code solution2.py %}
