---
title: 乐鑫科技 ESP32 Microcontroller Unit
notebook: notes
date: 2025-11-18 23:44:11
updated: 2025-11-18 23:44:11
tags:
  - it/embed
---
## Related Terminologies

### MCU

[MCU](http://www.htsemi.com/shows/18/96.html) 英文全称是 Microcontroller Unit，是指微控制单元又称单片微型计算机或者单片机，其实 MCU 就是单片机。MCU 其实也可以理解为简单版本的 CPU，就是把中央处理器的频率与规格做适当缩减，并将内存、计数器、USB、A/D 转换、UART、PLC、DMA 等周边接口，甚至 LCD 驱动电路都整合在单一芯片上，形成芯片级的计算机，为不同的应用场合做不同组合控制。

### SoC

SoC，是 System on Chip 的缩写，翻译过来就是系统级芯片，也有称 [片上系统](https://baike.baidu.com/item/%E7%89%87%E4%B8%8A%E7%B3%BB%E7%BB%9F)。既然是系统，单个就称不上系统，只有多个个体的组合才能称之为系统，所以，SoC 强调的是一个整体。用「麻雀虽小五脏俱全」来形容 SoC，再确切不过了。SoC 是模仿计算机系统，微缩成了一个微系统。

硬件的大概的组成是：核心（core），存储，外设接口（高速外设和低速外设），总线，中断模块，时钟模块等。在验证阶段，这些都是用 verilog 代码实现的，你是看不到实体的。先简单说一下这几个的概念，以后再逐一展开。核心类似于计算机中的 CPU（中央处理器），包含多个小模块，存储分为很多种，像 SRAM，DRAM，ROM 之类的；外设接口可以理解为芯片对外的通信接口，与外界交互的接口；总线就像一根藤，而核心、存储、外设就像挂在藤上的葫芦娃，总线是这些「葫芦娃」交流的窗口。

### 模组

模组，也就是模块化整合技术，是一种同时集成芯片和电子元件的一体化设备。模块拥有很强的可插拔性、可复用性和可升级性等特点，是现代电子产品中广泛采用的一种技术手段。

### 芯片、模组、开发板

ESP 产品主要有芯片（Soc）、模组（Module）以及开发板三种形式。它们是层层包含关系，如下图，从内到外分别是 Soc，Module 和整个开发板。

![芯片-模组-开发板](assets/espressif-esp32-mcu/20251109-213950.png)

## 乐鑫科技芯片

[芯片概览｜乐鑫科技](https://www.espressif.com.cn/zh-hans/products/socs)

- ESP32 [ESP32 Wi-Fi & 蓝牙 SoC ｜乐鑫科技](https://www.espressif.com.cn/zh-hans/products/socs/esp32)
    - 初代经典款，双核处理器（Xtensa LX6），支持 Wi-Fi 4 + 蓝牙 4.2，适用于通用物联网场景。
    - ESP32: 32-bit MCU & 2.4 GHz Wi-Fi & Bluetooth/Bluetooth LE
- ESP32-S
    - （"S" 代表性能升级）优化架构，增强安全性、外设功能，部分型号支持 AI 加速。
    - ESP32-S2: 32-bit MCU & 2.4 GHz Wi-Fi
        - 单核（Xtensa LX7），增加 USB OTG 功能。
    - ESP32-S3: 32-bit MCU & 2.4 GHz Wi-Fi & Bluetooth 5 (LE)
        - 双核（Xtensa LX7），支持蓝牙 5.0，AI 指令集加速。
    - ESP32-S4
        - （未量产）更高性能，专为 AIoT 设计。
- ESP32-C
    - （"C" 代表成本优化）精简设计，采用 RISC-V 架构，主打高性价比。
    - ESP32-C2: 32-bit RISC-V MCU & 2.4 GHz Wi-Fi & Bluetooth 5 (LE)
    - ESP32-C5: 32-bit RISC-V MCU & 2.4 and 5 GHz Wi-Fi 6 & Bluetooth 5 (LE) & IEEE 802.15.4
    - ESP32-C3: 32-bit RISC-V MCU & 2.4 GHz Wi-Fi & Bluetooth 5 (LE)
        - 单核 RISC-V，支持 Wi-Fi 4 + 蓝牙 5.0。
    - ESP32-C6: 32-bit RISC-V MCU & 2.4 GHz Wi-Fi 6 & Bluetooth 5 (LE) & IEEE 802.15.4
        - 双核 RISC-V，支持 Wi-Fi 6 + 蓝牙 5.3。
    - ESP32-C61: 32-bit RISC-V MCU & 2.4 GHz Wi-Fi 6 & Bluetooth 5 (LE)
- ESP32-H
    - （"H" 代表低功耗或特定协议）专注低功耗或特定无线协议（如 Thread/Zigbee）。
    - ESP32-H2: 32-bit RISC-V MCU & Bluetooth 5 (LE) & IEEE 802.15.4
        - 支持蓝牙 5.2 + IEEE 802.15.4（Zigbee/Thread）。
- ESP32-P
    - ESP32-P4: 32-bit RISC-V MCU
- ESP8266（早期版本）
    - ESP8266: 32-bit MCU & 2.4 GHz Wi-Fi

型号后缀含义：

- 数字（如 -CS、-C6）
    - 表示迭代版本，数字越大通常代表功能越新或性能越强
- 封装与 Flash 配置
    - -MINI: 小尺寸模块（如 ESP32-C3-MINI-1）
    - -4MB/-8MB: 内置 Flash 容量（如 ESP32-S3-8MB）
    - -N4/N8: 外置 Flash 配置（如 ESP32-C3FN4）
- 功能扩展
    - -V: 芯片版本（如 ESP32-S3-V1.1）
    - -PICO: 集成度高的小封装（如 ESP32-PICO-D4）

快速识别要点：

- 芯片架构：`C` 系列多为 RISC-V，`S` 系列为 Xtensa。
- 无线协议：`H` 系列支持低功耗协议，`C6`/`S3` 支持最新蓝牙/Wi-Fi。
- 性能定位：数字越大，功能越新（如 S3 > S2，C6 > C3）。

芯片命名规则：

{% invert %}
![ESP32 芯片命名规则](assets/espressif-esp32-mcu/20251109-225141.png)

![ESP32-S3 芯片命名规则](assets/espressif-esp32-mcu/20251109-225154.png)
{% endinvert %}

## 乐鑫科技模组

[模组概览｜乐鑫科技](https://www.espressif.com.cn/zh-hans/products/modules)

## 乐鑫科技开发板

乐鑫官方开发板通常以「ESP32-XX-DevKitX」格式命名。

如：ESP32-S3-DevKitC-1

- S3: 芯片型号
- DevKitC: 开发板类型（C 表示基础款）
- 1: 版本号

### ESP32 系列开发板

- [ESP32-DevKitC](https://docs.espressif.com/projects/esp-dev-kits/zh_CN/latest/esp32/esp32-devkitc/index.html)
    - 基于 ESP32 的小型开发板，板上模组的绝大部分管脚均已引出，开发人员可根据实际需求，轻松通过跳线连接多种外围器件，或将开发板插在面包板上使用。
- [ESP32-DevKitM-1](https://docs.espressif.com/projects/esp-dev-kits/zh_CN/latest/esp32/esp32-devkitm-1/index.html)
    - 基于 ESP32-MINI-1/1U 模组的入门级开发板。板上模组大部分管脚均已引出至两侧排针，用户可根据实际需求，通过跳线轻松连接多种外围设备，同时也可将开发板插在面包板上使用。
- [ESP32-PICO-KIT-1](https://docs.espressif.com/projects/esp-dev-kits/zh_CN/latest/esp32/esp32-pico-kit-1/index.html)
    - 最小开发板，可插接于迷你面包板。ESP32-PICO-KIT-1 为用户提供了基于 ESP32-PICO-V3 芯片开发应用程序的硬件，更加方便用户探索 ESP32 芯片的功能。
- [ESP32-PICO-DevKitM-2](https://docs.espressif.com/projects/esp-dev-kits/zh_CN/latest/esp32/esp32-pico-devkitm-2/index.html) ✅
    - 基于 [ESP32](https://www.espressif.com/zh-hans/products/socs/esp32) 的乐鑫开发板，板上搭载 [ESP32-PICO-MINI-02/02U](https://www.espressif.com/zh-hans/products/modules) 模组。ESP32-PICO-MINI-02/02U 模组具备完整的 Wi-Fi 和蓝牙功能。
    - [ESP32-PICO-DevKitM-2 开发板](ESP32-PICO-DevKitM-2%20开发板.md)
- [ESP32-LCDKit](https://docs.espressif.com/projects/esp-dev-kits/zh_CN/latest/esp32/esp32-lcdkit/index.html)
    - 以乐鑫 ESP32-DevKitC（需另采购）为核心的 HMI（人机交互）开发板。
- [ESP32-Ethernet-Kit](https://docs.espressif.com/projects/esp-dev-kits/zh_CN/latest/esp32/esp32-ethernet-kit/index.html)
    - 以太网转 Wi-Fi 开发板，可为以太网设备赋予 Wi-Fi 连接功能。

寿命终止开发板：

- [ESP32-Sense-Kit](https://docs.espressif.com/projects/esp-dev-kits/zh_CN/latest/esp32/esp32-sense-kit/index.html)
- [ESP32-MeshKit-Sense](https://docs.espressif.com/projects/esp-dev-kits/zh_CN/latest/esp32/esp32-meshkit-sensor/index.html)
- [ESP-WROVER-KIT](https://docs.espressif.com/projects/esp-dev-kits/zh_CN/latest/esp32/esp-wrover-kit/index.html)
- [ESP32-PICO-KIT](https://docs.espressif.com/projects/esp-dev-kits/zh_CN/latest/esp32/esp32-pico-kit/index.html)
