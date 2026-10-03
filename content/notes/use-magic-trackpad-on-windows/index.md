---
title: 在 Windows 中使用 Magic Trackpad
notebook: notes
tags:
- hardware
date: 2025-04-26 23:20:57
updated: 2026-04-15 22:02:48
references:
- '[Win11使用magic trackpad （苹果妙控板） - 知乎](https://zhuanlan.zhihu.com/p/608208531)'
---
在 Windows 系统中使用苹果的 Magic Trackpad（妙控板）。

## 驱动

[vitoplantamura/MagicTrackpad2ForWindows: Magic Trackpad 2 Precision Touchpad driver for Windows 11, based on the imbushuo driver, signed by Microsoft](https://github.com/vitoplantamura/MagicTrackpad2ForWindows)

{% badge_github vitoplantamura MagicTrackpad2ForWindows release:true %}

下载 release 压缩包，右键点击驱动文件 `./AMD64/AmtPtpDevice.inf`，选择「Install」。

> [!caution]
> Uninstall any previous versions of this driver, the old imbushuo's version or `official 2021 Apple driver`.

- 有线模式：给 Magic Trackpad 开机，用 USB 线连到电脑上，即可 👍。
- 蓝牙模式：如果搜不到设备，可以关闭 Magic Trackpad 然后再打开（可能是刚打开的时候才能搜的到）。不确定是否一定要拔掉 USB 线。

调节配置：在 Windows 中进入 Settings -> Bluetooth & devices -> Touchpad。

压缩包里的 `AmtPtpControlPanel.exe` 可以直接运行，提供了一些额外的控制，以及电量查看（限蓝牙模式）。

## Tips

### Unable to Click-and-Drag

[Unable to click-and-drag · Issue #15 · vitoplantamura/MagicTrackpad2ForWindows](https://github.com/vitoplantamura/MagicTrackpad2ForWindows/issues/15)

> Pressing down to click then dragging results in the mouse pointer remaining still. Not only is click-and-drag support missing, the mouse stops moving entirely while my finger remains pressing down.

运行 `AmtPtpControlPanel.exe`，取消「Ignore input from the finger used to click the force button」即可。

## 旧版驱动 (by imbushuo, 2021)

[imbushuo/mac-precision-touchpad: Windows Precision Touchpad Driver Implementation for Apple MacBook / Magic Trackpad](https://github.com/imbushuo/mac-precision-touchpad)

缺点：

1. 有点儿过于灵敏，有时候会造成误触（比如本来只是在移动鼠标，但手的其他部位不小心轻轻碰到了 Magic Trackpad，就会变成缩放操作）。把灵敏度调到最低也比在 macOS 中「过敏」一些。
2. 蓝牙模式下，无法看到剩余电量。
3. 原作者已经不更新了。

