---
title: 给 HHKB 增加 YDKB 蓝牙模块
notebook: notes
tags:
  - hardware
  - calf
date: 2024-06-11 16:52:29
updated: 2025-04-23 00:01:29
---
## 背景

HHKB Professional 2 Type-S 静电容键盘，2015 年购入，型号 `PD-KB400WS`，不带蓝牙。

2019 年找到 YDKB 客制化 HHKB 蓝牙主控，入手后替换掉原厂主控，之后日常使用蓝牙模式。

## YDKB 蓝牙模块

[YDKB静电容改无线蓝牙BLE BT双模主控非键盘，适用HHKB Pro2系列-淘宝网](https://item.taobao.com/item.htm?spm=2013.1.0.0.55833129b2R2LL&id=590221409485)

需要自行拆开键盘后盖，替换掉原厂主控板。按宝贝详情页的说明操作即可，无需焊接。

- [YDKB Document](https://ydkb.io/help/#/)
- [YD Keymap Builder for HHKB BLE](https://ydkb.io/?hhkb_ble)

### 主要特性

- 整个改装无需焊接，只需要拧螺丝拔排线换主控，非常容易。
- USB / 蓝牙 4.0 双模，插线时可在有线或蓝牙间切换，充电也是直接通过 USB 接口。
- USB 下支持全键无冲（可通过左右 {% kbd Shift %} + {% kbd N %} 切换），蓝牙下支持任意 6 键无冲。
- 全键位都支持自定义，固件功能基于 tmk，使用 [ydkb.io](https://ydkb.io/) 图形化工具，简单易懂。
- 使用标准 3.7v 锂电（默认不带电池），可自备，也可选购买本店定制的 2500mAh 电池。
- 支持自动节能，极速唤醒。独创 Lock Mode，可防止键盘放包里按键被压耗电，携带更轻松。
- 大部分系统支持电量显示（Mac 需要第三方软件或用文字输出）。键盘也自带有低电量提醒。
- USB HUB（USB 2.0，仅有线模式可用），主要是为了美观。共三个，两外置一内置。
- 主控自带充电和 LED3 两个指示灯。正面还支持安装三个指示灯（LED1、2、3）。
  - 注：三个指示灯只有白色外壳可以透。

更新：至少从 2023 年，macOS 系统蓝牙连接那里就已经可以直接显示出键盘剩余电量了。

补充一条：这个比官方的蓝牙版本还要好，官方版本键盘后边突出来一大块用来装电池，但这个是内置了锂电池，通过 USB 充电。

### LED 指示灯状态

- 刷机模式（空闲）：三个指示灯一起闪或者交替闪，一直不灭。
- 刷机模式（数据写入）：在上面基础上，LED3 快速闪烁。
- 启动时蓝牙 未连接 状态指示：LED3 闪烁，如果一直未连接，约 15 秒左右会停止闪烁。
- 启动时蓝牙 已连接 状态指示：LED2 和 LED3 同时较慢闪。每次亮的时间明显长于灭的时间。
- 按键 {% kbd LShift %} + {% kbd RShift %} + {% kbd S %}：按上面的方式指示蓝牙连接状态。
- 手动进入 Lock Mode：三个灯同时亮起，然后再按 LED3 LED2 LED1 的顺序依次熄灭。
- 从二级节能或 Lock Mode 唤醒：三个灯同时亮起，然后开始指示蓝牙连接状态。
- 低电量提示：用键盘时，三个灯同时闪；节能时不闪。依然还可以使用两三天。
- 极低电量提示：用键盘时，三个灯同时飞快闪；节能时不闪。此时建议尽快充电。

### 节能模式说明

日常使用时键盘会自动节能，不用时也不需要关闭电池开关。

1. 键盘闲置 3 秒没按任何按键后，进入一级节能。此模式下，检测按键频率降低，但是唤醒很快。
2. 键盘 90 秒蓝牙未连接，或 2.5 小时未使用，进入二级节能。长按任意键 3 到 5 秒可以唤醒。
3. 使用 Lock Mode，会直接进入二级节能，与 2 的区别是，此时，只有同时且仅长按 {% kbd F %} 和 {% kbd J %} 唤醒，其他键不行。

## 使用信息和常见故障排查

- [BLE 系列排错指南](https://ydkb.io/help/#/ble-series/troubleshooting)
- [BLE 系列说明(总览)](https://ydkb.io/help/#/ble-series/)

### 查看剩余电量

新的 macOS 系统中，蓝牙连接那里就可以显示出键盘的剩余电量。

按 {% kbd Fn %} + {% kbd E %}，可以通过键盘输出剩余电量的值，如 `70-1`。

按 {% kbd LShift %} + {% kbd RShift %} + {% kbd V %} 也可以输出剩余电量值。

### 查询和升级固件

[YDKB 固件更新 - 查看当前固件版本](https://ydkb.io/help/#/firmware?id=%e6%9f%a5%e7%9c%8b%e5%bd%93%e5%89%8d%e5%9b%ba%e4%bb%b6%e7%89%88%e6%9c%ac)

通过 USB 线连接到电脑上，在设备管理里 USB 设备中查看设备名，如 `HHKB BLE (USB_DL9M)`，其中 `L9M` 对应了固件的版本日期 2021-09-22。

> 好像直接用 type-C 线连到电脑的 type-C 口上不行，用 type-C 转 USB 的 hub 加上 usb 转 type-C 的连线可以。

三位日期计法速查表：

| 年   | 19 | 20 | 21 | 22 | 23 | 24 |
|------|----|----|----|----|----|----|
| 计法 | J  | K  | L  | M  | N  | O  |
| 年   | 25 | 26 | 27 | 28 | 29 | 30 |
| 计法 | P  | Q  | R  | S  | T  | U  |

| 月   | 1...9 | 10 | 11 | 12 |
|------|-------|----|----|----|
| 计法 | 1...9 | A  | B  | C  |

| 日 | 1...9 | 10 | 11 | 12 | 13 | 14 |
|----|-------|----|----|----|----|----|
| 计 | 1...9 | A  | B  | C  | D  | E  |
| 日 | 15    | 16 | 17 | 18 | 19 | 20 |
| 计 | F     | G  | H  | I  | J  | K  |
| 日 | 21    | 22 | 23 | 24 | 25 | 26 |
| 计 | L     | M  | N  | O  | P  | Q  |
| 日 | 27    | 28 | 29 | 30 | 31 |    |
| 计 | R     | S  | T  | U  | V  |    |

[HHKB BLE 固件记录](https://ydkb.io/help/#/changelog/hhkb_ble)

访问 [YD Keymap Builder for HHKB BLE](https://ydkb.io/?hhkb_ble)，可以查看最新固件版本号、固件更新历史，下载最新版固件文件（HHKB_BLE.BIN）。

macOS 13 以上的系统，需要按照 [Bootloader, Flash Firmware - Reflash firmware in Mac](https://ydkb.io/help/#/en/bootloader/msd-bootloader?id=reflash-firmware-in-mac) 进行固件刷新。

1. 下载最新的固件文件 `HHKB_BLE.BIN`。
2. 按住 {% kbd ESC %} 键的同时，插入 USB 连线。电脑上会出现名为 `HHKB_BLE` 的磁盘。
3. `diskutil umount /Volumes/HHKB_BLE`
   1. 会提示 `Volume HHKB_BLE on disk2 unmounted`，其中 `disk2` 可能会不一样。
4. `sudo dd if=./HHKB_BLE.BIN of=/dev/disk2 seek=4`，注意如果上一步提示的不是 `disk2` 则需要替换一下。

Windows 简单一些，按照 [Bootloader, Flash Firmware - Reflash firmware in Windows](https://ydkb.io/help/#/en/bootloader/msd-bootloader?id=reflash-firmware-in-windows) 操作即可。

1. 下载最新的固件文件 `HHKB_BLE.BIN`。
2. 按住 {% kbd ESC %} 键的同时，插入 USB 连线。电脑上会出现名为 `HHKB_BLE` 的磁盘。
3. 把 `HHKB_BLE.BIN` 拖到该磁盘根目录，覆盖掉同名文件，然后弹出设备（一般会自动弹出）即可。

### 修改按键

修改按键对应的功能，跟刷固件的操作一致。只要在 [YD Keymap Builder for HHKB BLE](https://ydkb.io/?hhkb_ble) 页面里先做好期望的调整，再下载的固件文件中就包含所做的设置。

比如在习惯了 macOS 之后，如果在 Windows 中用 HHKB，经常按错快捷键，可以考虑把 {% kbd Ctrl %} 键和 {% kbd ⌘ Cmd %}（即 {% kbd ⊞ Win %} 键）互换。

### 蓝牙连接无法自动连上

2024-06-11

换了新电脑，通过 timemachine 同步了原电脑的数据，但键盘无法自动连接，每次连接断开之后，都只能选择 forget 设备，然后再手动连接。

需要在键盘上清除配对信息：先删除，然后配对前键盘那边先执行清除配对一次，再重新配对。

[BLE 系列排错指南 - 蓝牙无法自动连接](https://ydkb.io/help/#/ble-series/troubleshooting?id=%e8%93%9d%e7%89%99%e6%97%a0%e6%b3%95%e8%87%aa%e5%8a%a8%e8%bf%9e%e6%8e%a5)

1. 先删除电脑上已经配对的该蓝牙键盘。
2. 在键盘上按 {% kbd LShift %} + {% kbd RShift %} + {% kbd LCtrl %} + {% kbd R %}，清除键盘端保存的配对信息。
3. 设备搜索键盘，重新配对一次。
