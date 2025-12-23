---
title: 2241. Design an ATM Machine
notebook: coding
tags:
- medium
date: 2025-01-05 10:36:09
updated: 2025-01-05 10:36:09
---
## Problem

There is an ATM machine that stores banknotes of `5` denominations: `20`, `50`, `100`, `200`, and `500` dollars. Initially the ATM is empty. The user can use the machine to deposit or withdraw any amount of money.

When withdrawing, the machine prioritizes using banknotes of **larger** values.

- For example, if you want to withdraw `$300` and there are `2` `$50` banknotes, `1` `$100` banknote, and `1` `$200` banknote, then the machine will use the `$100` and `$200` banknotes.
- However, if you try to withdraw `$600` and there are `3` `$200` banknotes and `1` `$500` banknote, then the withdraw request will be rejected because the machine will first try to use the `$500` banknote and then be unable to use banknotes to complete the remaining `$100`. Note that the machine is **not** allowed to use the `$200` banknotes instead of the `$500` banknote.

Implement the ATM class:

- `ATM()` Initializes the ATM object.
- `void deposit(int[] banknotesCount)` Deposits new banknotes in the order `$20`, `$50`, `$100`, `$200`, and `$500`.
- `int[] withdraw(int amount)` Returns an array of length `5` of the number of banknotes that will be handed to the user in the order `$20`, `$50`, `$100`, `$200`, and `$500`, and update the number of banknotes in the ATM after withdrawing. Returns `[-1]` if it is not possible (do **not** withdraw any banknotes in this case).

<https://leetcode.cn/problems/design-an-atm-machine/>

**Example 1:**

> Input
> `["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"]`
> `[[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]`
> Output
> `[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]`
> Explanation
>
> ``` c++
> ATM atm = new ATM();
> atm.deposit([0,0,1,2,1]); // Deposits 1 $100 banknote, 2 $200 banknotes,
> // and 1 $500 banknote.
> atm.withdraw(600);        // Returns [0,0,1,0,1]. The machine uses 1 $100 banknote
> // and 1 $500 banknote. The banknotes left over in the
> // machine are [0,0,0,2,0].
> atm.deposit([0,1,0,1,1]); // Deposits 1 $50, $200, and $500 banknote.
> // The banknotes in the machine are now [0,1,0,3,1].
> atm.withdraw(600);        // Returns [-1]. The machine will try to use a $500 banknote
> // and then be unable to complete the remaining $100,
> // so the withdraw request will be rejected.
> // Since the request is rejected, the number of banknotes
> // in the machine is not modified.
> atm.withdraw(550);        // Returns [0,1,0,0,1]. The machine uses 1 $50 banknote
> // and 1 $500 banknote.
> ```

**Constraints:**

- `banknotesCount.length == 5`
- `0 <= banknotesCount[i] <= 10⁹`
- `1 <= amount <= 10⁹`
- At most `5000` calls **in total** will be made to `withdraw` and `deposit`.
- At least **one** call will be made to each function `withdraw` and `deposit`.
- Sum of `banknotesCount[i]` in all deposits doesn't exceed `10⁹`

## Test Cases

``` python
class ATM:

    def __init__(self):


    def deposit(self, banknotesCount: List[int]) -> None:


    def withdraw(self, amount: int) -> List[int]:



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
```

{% asset_code coding/2241-design-an-atm-machine/solution_test.py %}

## Thoughts

开始以为类似 [322. Coin Change](../322-coin-change/index.md) 或 [494. Target Sum](../494-target-sum/index.md)，结果没那么复杂，是个比较「弱智」的机器。直接用贪心法，从最大面值的钞票开始，如果金额大于钞票面额就优先用此钞票。

存入和取出的时间复杂度都是 `O(1)`，空间复杂度 `O(1)`。

## Code

{% asset_code coding/2241-design-an-atm-machine/solution.py %}
