---
title: 利用不均匀硬币产生等概率
slug: unbalanced-coin
date: '2011-10-08T22:49:00+08:00'
lastmod: '2011-10-09T15:05:00+08:00'
tags:
- Interview Question
- Probability
categories:
- 算法
summary: 问题描述：有一枚不均匀的硬币，已知抛出此硬币后，正面向上的概率为 p（0 \< p \< 1）。请利用这枚硬币产生出概率相等的两个事件。
keywords:
- 不均匀硬币
- 概率
- 算法题
- 面试题
---

问题描述：有一枚不均匀的硬币，已知抛出此硬币后，正面向上的概率为 p（0
\< p \< 1）。请利用这枚硬币产生出概率相等的两个事件。

这个问题跟之前的 [利用等概率 Rand5 产生等概率 Rand3](../build-rand3-from-rand5/index.md) 非常像，但却简单的多。几个月前还为这个事情头疼了一下，现在想来真是不应该。

某一次抛出硬币，正面向上的概率是 p，反面向上的概率是 1 \-
p，当 p 不等于 0\.5 时，这两个事件的概率就不一样了。怎么能凑出等概率呢？还是要利用概率的加法和乘法法则。这里用乘法，也就是连续的独立事件。

连续抛两次硬币，正反面的出现有四种情况，概率依次为：

1. 两次均为正面：p \* p


2. 第一次正面，第二次反面：p \* \(1 \- p\)


3. 第一次反面，第二次正面：\(1 \- p\) \* p


4. 两次均为反面：\(1 \- p\) \* \(1 \- p\)


这不，中间两种情况的概率是完全一样的。于是问题的解法就是连续抛两次硬币，如果两次得到的相同则重新抛两次；否则根据第一次（或第二次）的正面反面情况，就可以得到两个概率相等的事件。

用 Python 程序模拟一下这个过程，首先是一个叫做 ` UnbalancedCoin ` 的类，用来模拟这枚不均匀的硬币。Flip 方法表示抛一次硬币，返回值 True 代表正面，False 代表反面。根据要求，这个函数返回 True 和 False 的概率分别是 p 和 1
\-
p。函数 ` MakeEqualProb ` 利用参数 ` coin `（这枚不均匀硬币）构造出两个事件（依旧用 True 和 False 表示），并且这两个事件的概率都是 0\.5。

````python {linenos=table}
from random import Random

class UnbalancedCoin:
  def __init__(self, p, rand=None):
    assert 0.0 < p < 1.0, 'invalid p'
    self._p = p
    if rand is None:
      rand = Random()
    self._rand = rand

  def Flip(self):
    return self._rand.random() < self._p

def MakeEqualProb(coin):
  while True:
    a = coin.Flip()
    if a != coin.Flip():
      return a
````

对于不同的 p 值，模拟实验十万次，得到如下的（结果为 True 的）概率分布，其中蓝线是不均匀硬币抛出后正面向上的概率，红线是构造出来的两个事件之一（第一次正面向上，第二次反面向上）的概率。

{{< image src="coin-prob-chart.svg" alt="coin-prob-chart" caption="coin-prob-chart（静态图）" >}}

[原始数据（JSON）](coin-prob-chart.json)

如果问题改变一下，把“一枚”改成“一种”，那解决办法就更简单有趣了，把两枚同样的不均匀硬币正面相对粘在一起，就可以得到一个均匀的组合币，抛出这枚组合币就可以得到等概率的两个事件。
