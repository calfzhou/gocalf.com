---
title: 准备改用 RIME 系列的输入法
date: 2024-04-23 21:33:11
updated: 2024-07-27 22:35:07
---

前几天在 Clash 的 connections 列表中看到一大片搜狗输入法的网络连接，很多都持续了很多天甚至一两个月。是该考虑换个输入法了。

说起输入法，最早开始用的非系统自带的输入法就是当年大名鼎鼎的紫光输入法。多年之后，Google 推出了他们的中文输入法，做为 G 粉当然是切换到了 Google 输入法，一用又是很多年。记不清后来具体因为什么，好像 Google 也不太维护它了，好像 macOS 里不太能用，总之中间经过一段时间的凑活之后，就一直在用搜狗输入法，macOS 和 iOS 上都是，且登录了账号进行配置和词库同步。

现在想来，还是得考虑改用开源输入法了。稍微搜了一下，几乎都会提到 [RIME | 中州韻輸入法引擎](https://rime.im/)，[rime/librime: Rime Input Method Engine, the core library](https://github.com/rime/librime)。

{% badge_github rime librime release:true %}

{% quot RIME | 聪明的输入法懂我心意 %}

RIME 本身是一个输入法算法框架。基于这一框架，Rime 开发者与其他开源社区的参与者在 Windows、macOS、Linux、Android 等平台上创造了不同的输入法前端实现。

比如 macOS 里的叫 鼠须管（Squirrel），[rime/squirrel: 【鼠鬚管】Rime for macOS](https://github.com/rime/squirrel)。

{% badge_github rime squirrel release:true %}

Windows 里的叫 小狼毫（Weasel），[rime/weasel: 【小狼毫】Rime for Windows](https://github.com/rime/weasel)。

{% badge_github rime weasel release:true %}

其他系统/平台的客户端信息参见 [下載及安裝 | RIME | 中州韻輸入法引擎](https://rime.im/download/)。

iOS 上目前暂时用的是 Hamster（「仓」输入法），[imfuxiao/Hamster: librime for iOS App](https://github.com/imfuxiao/Hamster)。

{% badge_github imfuxiao Hamster release:true %}

不过整体上，还只是安装和试用了，还没有完全切换过去，还是有很多不适应的地方。

Squirrel 装完了，打字只有繁体，说是按 {% kbd Ctrl %} + {% kbd ` %} 或者 {% kbd F4 %} 可以呼出方案选单，切换输入方式，但是完全出不来。后来第二天又装了一次，终于可以了，至少先切换成简体，先用起来。

跟普通的商业公司出品的输入法比起来，这个系列的最大特点恐怕就是：

{% quot 这是一款需要折腾的输入法 %}

输入法的 [Wiki](https://github.com/rime/home/wiki) 我都还没有看完（就还没怎么看）。而没有做精细的配置之前，使用体验上比搜狗还是差很多的。比如搜狗里首屏会出现一些常用的 emoji 或者标点；按 `u` 可以进行笔画输入或者拼音字组合；中文输入状态如果输入的是英文单词，也会有合理的提示；中文和英文或数字之间会自动加空格；手机上英文键盘也支持滑动输入大小写或者符号，等等。

当然应该不是输入法不好，只是我还没研究。有空了再研究吧，希望不会是从安装到放弃。

【2024-07-27】四月份装了 Squirrel 之后，尝试了几天，后来就一直没再使用。这次下定决心要切换了，重新研究了一翻，配置了雾凇拼音，整体输入体验很好。把电脑上的搜狗输入法卸载掉了。
