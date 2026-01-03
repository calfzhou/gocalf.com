---
title: Hledger
notebook: notes
tags:
  - software
date: 2026-01-03 23:47:28
updated: 2026-01-03 23:47:28
---
## Info

[Home - hledger](https://hledger.org/)

{% badge_github simonmichael hledger release:true %}

> **hledger** is friendly, fast, and dependable accounting software for tracking money, investments, cryptocurrencies, time, or any countable commodity. It uses human-readable **[plain text data](https://plaintextaccounting.org/)** that you control.

[hledger manual (1.51) » Journal](https://hledger.org/1.51/hledger.html#journal)

> hledger's usual data source is a plain text file containing journal entries in hledger `journal` format.

## 基本使用

```bash
brew install hledger

hledger --version
#> hledger 1.51.1, mac-x86_64
```

例行核对：

```bash
hledger bal [-f xxx.journal]
```

如果某个账户余额核对出错，可以列出其相关交易以便排查：

``` bash
hledger reg [-f xxx.journal] -I 'Assets:Online:WeChat$' cur:CNY
```

检查 transactions 是按日期有序排列的：

```bash
hledger check ordereddates [-f xxx.journal]
```

## 更新注意

### 1.50 - Transaction Balancing

> Transaction balancing is now done in a more robust way, using local precisions only (like Ledger) [#2402](https://github.com/simonmichael/hledger/pull/2402). Until now, a transaction was required to balance using its commodities's global display precisions. Small imbalances were tolerated by configuring display precisions for the whole journal (with `commodity` directives).

比如这条 transaction 在 1.50+ 就不行：

```text
339 | 2013-01-30 计算持仓均价
    |     Assets:Investment:ICBC:PaperSilver    600 XAGg @ 6.2454167 CNY
    |     Assets:Investment:ICBC:PaperSilver      -100 XAGg @ 6.2175 CNY
    |     Assets:Investment:ICBC:PaperSilver       -500 XAGg @ 6.251 CNY

This transaction is unbalanced.
The real postings' sum should be 0 but is: 0.0000200 CNY
Note, hledger <1.50 accepted this entry because of the global display precision,
but hledger 1.50+ checks more strictly, using the entry's local precision.
```

因为后两条的总额相当于 37.4725 CNY，除以 6 无法除尽，`@ 6.2454167 CNY` 无论保留多少位都没办法。

对于这种场景，直接不做这种均价化的处理了（至少不在除不尽的时候做），缺点是要自己管理「先入先出」。

另一种情况：

```text
292 | 2024-02-01 饮料
    |     Expenses:Catering:Drink             380 JPY @ 0.049572 CNY
    |     Liabilities:Credit:ICBC:Visa2643     -2.6 USD @ 7.2451 CNY

This multi-commodity transaction is unbalanced.
The real postings' sum should be 0 but is: 0.000100 CNY
Note, hledger <1.50 accepted this entry because of the global display precision,
but hledger 1.50+ checks more strictly, using the entry's local precision.
```

这里的误差就没法避免了，因为银行在记账的时候做了舍入处理。考虑引入特殊的 account 来 absorb the imbalance：

```hledger
2024-02-01 饮料
    Expenses:Catering:Drink             380 JPY @ 0.049572 CNY
    Liabilities:Credit:ICBC:Visa2643    -2.6 USD @ 7.2451 CNY
    Expenses:Misc:Rounding              -0.0001 CNY
```

如果前两行的 `@ UNITPRICE` 都没有问题，也可以省略 `Expenses:Misc:Rounding` 的金额，让 hledger 自动计算。
或者使用 `@@ TOTALPRICE` 语法，避开除不尽的 `@ UNITPRICE`：

```hledger
2024-02-01 饮料
    Expenses:Catering:Drink             380 JPY @@ 18.83726 CNY
    Liabilities:Credit:ICBC:Visa2643    -2.6 USD @ 7.2451 CNY
```

## 实践

### 按年拆分 Journal

一年一个 Journal 文件，日常只处理当年的文件，需要的时候可以把连续若干年的文件「连」起来一并处理。

用 `hledger close` 命令生成 closing 文件和 opening 文件。

设起始年是 2000 年，记录于 `2000.journal` 文件。在 2000 年结束后，运行：

```bash
hledger close -f 2000.journal \
    --close --show-costs \
    -e 2001 --close-acct Equity:OpeningClosing:2001 \
    Assets Liabilities > export/2000-closing.journal

hledger close -f 2000.journal \
    --open --show-costs \
    -e 2001 --close-acct Equity:OpeningClosing:2001 \
    Assets Liabilities > export/2001-opening.journal
```

> 👆 `Assets Liabilities` 是默认会带到 closing 或 opening 的 accounts，可以指定任何 accounts。

生成 2000 年的 closing journal 和 2001 年的 opening journal：

```hledger export/2000-closing.journal
2000-12-31 closing balances  ; clopen:2001
    Assets:Cash                          -48.90 CNY = 0.00 CNY
    Assets:Checking:ICBC:Foo          -2,913.60 CNY = 0.00 CNY
    Assets:Deposit:Unknown:Fixed     -11,000.00 CNY = 0.00 CNY
    Equity:OpeningClosing:2001
```

```hledger export/2001-opening.journal
2001-01-01 opening balances  ; clopen:2001
    Assets:Cash                          48.90 CNY = 48.90 CNY
    Assets:Checking:ICBC:Foo          2,913.60 CNY = 2,913.60 CNY
    Assets:Deposit:Unknown:Fixed     11,000.00 CNY = 11,000.00 CNY
    Equity:OpeningClosing:2001
```

在 `2001.journal` 开头 include 其 opening journal：

```hledger 2001.journal
include share/commodities.journal
include export/2001-opening.journal

; Default year.
Y2001
; Default commodity.
D 1,000.00 CNY

; transactions
```

可以创建一个文件，比如叫作 `active.journal`：

```hledger active.journal
include share/accounts.journal
include 2001.journal
```

可以设定环境变量 `LEDGER_FILE` 的值为此文件的路径，那么执行 hledger 命令时就默认使用这个文件。

如果想把所有年份的 journal 放在一起处理，可以创建一个文件，比如 `all.journal`：

```hledger all.journal
include share/accounts.journal

include 2000.journal
include export/2000-closing.journal
include 2001.journal
include export/2001-closing.journal
include 2002.journal
; ...
```

