---
title: 在 Windows 中使用 Magic Trackpad
notebook: notes
tags:
- hardware
date: 2025-04-26 23:20:57
updated: 2025-04-26 23:20:57
references:
- '[Win11使用magic trackpad （苹果妙控板） - 知乎](https://zhuanlan.zhihu.com/p/608208531)'
---
在 Windows 系统中使用苹果的 Magic Trackpad（妙控板）。

[imbushuo/mac-precision-touchpad: Windows Precision Touchpad Driver Implementation for Apple MacBook / Magic Trackpad](https://github.com/imbushuo/mac-precision-touchpad)

[<img alt="imbushuo/mac-precision-touchpad" src="https://img.shields.io/static/v1?label=imbushuo&message=mac-precision-touchpad&color=blue&logo=github" style="display: inline-block">](https://github.com/imbushuo/mac-precision-touchpad) <img alt="stars" src="https://img.shields.io/github/stars/imbushuo/mac-precision-touchpad?logo=.&style=social" style="display: inline-block"> <img alt="forks" src="https://img.shields.io/github/forks/imbushuo/mac-precision-touchpad?logo=.&style=social" style="display: inline-block"> <img alt="updated" src="https://img.shields.io/github/last-commit/imbushuo/mac-precision-touchpad?label=" style="display: inline-block"> <img alt="release" src="https://img.shields.io/github/v/release/imbushuo/mac-precision-touchpad?label=" style="display: inline-block"> <img alt="release date" src="https://img.shields.io/github/release-date/imbushuo/mac-precision-touchpad?label=" style="display: inline-block">

下载上述驱动，比如 [Drivers-amd64-ReleaseMSSigned.zip](https://github.com/imbushuo/mac-precision-touchpad/releases/download/2105-3979/Drivers-amd64-ReleaseMSSigned.zip)。

解压缩后，右键点击 `./drivers/amd64/AmtPtpDevice.inf`，选择 "Install"。

给 Magic Trackpad 开机，用 USB 线连到电脑上，即可 👍。

用蓝牙模式（笔记本内置蓝牙，或者台式机插一个蓝牙适配器），如果搜不到设备，可以关闭 Magic Trackpad 然后再打开（可能是刚打开的时候才能搜的到）。不确定是否一定要拔掉 USB 线。

调节配置，在 Windows 中进入 Settings -> Bluetooth & devices -> Touchpad。

目前缺点：

1. 有点儿过于灵敏，有时候会造成误触（比如本来只是在移动鼠标，但手的其他部位不小心轻轻碰到了 Magic Trackpad，就会变成缩放操作）。把灵敏度调到最低也比在 macOS 中「过敏」一些。
2. 蓝牙模式下，无法看到剩余电量。
3. 原作者已经不更新了，最后一个版本是 2021 年的。
