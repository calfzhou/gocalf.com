---
title: 小智 AI 聊天机器人
notebook: notes
tags:
  - it/embed
  - it/ai
date: 2025-12-27 21:45:47
updated: 2025-12-27 21:45:47
---
## Info

[78/xiaozhi-esp32: An MCP-based chatbot | 一个基于MCP的聊天机器人](https://github.com/78/xiaozhi-esp32)

> 让我们一起探索人工智能与机器人技术的迷人世界！

{% badge_github 78 xiaozhi-esp32 release:true %}

小智的官方服务器 [Xiaozhi](https://xiaozhi.me/)

⭐ [⁢小智 AI 聊天机器人百科全书 - 飞书云文档](https://ccnphfhqs21z.feishu.cn/wiki/F5krwD16viZoF0kKkvDcrZNYnhb)

## DIY 硬件

ESP32-S3 开发板：[​小智AI聊天机器人面包板DIY硬件清单与接线教程 - 飞书云文档](https://ccnphfhqs21z.feishu.cn/wiki/EH6wwrgvNiU7aykr7HgclP09nCh)

- 开发板：ESP32-S3-DevKitC-1（选择 WROOM N16R8 模组）
    - 选 N16R8 模组，即 16 MB Flash 和 8 MB PSRAM 的配置
- 数字麦克风：INMP441 / ICS43434
- 功放：MAX98357A
- 腔体喇叭：8Ω 2~3W 或 4Ω 2~3W
- 导线：跳线一盒，杜邦线若干
- 400 孔面包板 2 块
- 128x32 I2C (IIC) 液晶显示屏，SSD1306 驱动（推荐）
- ML307R Cat.1 4G 模组，AT 固件版（可选）
- 6\*6mm 立式 轻触开关（可选）

其他：

- ESP32-C3 [​ESP32-C3小智AI终端面包板DIY硬件接线教程 - 飞书云文档](https://rcnv1t9vps13.feishu.cn/wiki/PovjwxG8tiEDrVkybstcqOz0nzf)
- ESP32 [⁤ESP32面包板-小智AI 制作说明 - 飞书云文档](https://hcngjtwigghb.feishu.cn/wiki/CmZxwV17miwpYHk46ZpcXutOnJ8)

### 功放 MAX98357A

引脚：

- VCC: 电源正极，DC 2.5V~5.5V
- GND: 接地
- SD: 关机和频道选择。`SD_MODE` 拉低以将器件置于关端状态。
- GAIN: 增益和频道选择。在 TDM 模式下，增益固定为 12dB。
- DIN: 数字输入信号
- BCLK: 位时钟信号
- LRC: I2S 与 LJ 模式的左/右时钟。同步时钟用于 TDM 模式。

### 接线

| ESP32-S3 | 麦克风 INMP441 | Note     |
| -------- | ----------- | -------- |
| GPIO4    | WS          | 数据选择     |
| GPIO5    | SCK         | 数据时钟     |
| GPIO6    | SD          | 数据输出     |
| 3V3      | VDD         | 电源正 3.3V |
| GND      | GND         | 接地       |
| GND      | L/R         | 左/右声道    |

| ESP32-S3 | 数字功放 MAX98357A | Note                  |
| -------- | -------------- | --------------------- |
| GPIO7    | DIN            | 数字信号                  |
| GPIO15   | BCLK           | 位时钟                   |
| GPIO16   | LRC            | 左/右时钟                 |
| 3V3      | Vin or VCC     | 电源                    |
| 3V3      | SD             | 关机频道                  |
| GND      | GND            | 接地                    |
|          | GAIN           | 增益和频道（BGA 封装（芯片小的）不用） |

| ESP32-S3 | 显示屏（IIC / I2C 接口） | Note |
| -------- | ----------------- | ---- |
| GPIO41   | SDA               | 数据线  |
| GPIO42   | SCK               | 时钟线  |
| 3V3      | VCC               | 电源   |
| GND      | GND               | 接地   |

| ESP32-S3 | 其他      | Note     |
| -------- | ------- | -------- |
| GPIO39   | 音量键按钮   | 另一头接 GND |
| GPIO40   | 音量加按钮   | 另一头接 GND |
| GPIO0    | BOOT 按钮 | 另一头接 GND |

## 自定义开发板

[xiaozhi-esp32/docs/custom-board.md 自定义开发板指南](https://github.com/78/xiaozhi-esp32/blob/main/docs/custom-board.md)

## Known Issues

### 只能语音唤醒

[添加远程唤醒MCP,能唤醒有文字返回，就是没有声音 · Issue #1215 · 78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32/issues/1215)

[mqtt+udp通信问题 · Issue #503 · 78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32/issues/503)

> 对于发起对话，Websocket是没有太多限制的。目前MQTT+UDP协议规定了，需要设备端先发送语音，语音通道才能成功建立，否则服务器无法知道设备端的UDP地址。

### 服务器自动结束对话

[用户长时间没有说话，你可以告别后主动结束会话。这个可以手动关闭吗？角色里说了不需要告别，但有时候一分钟后还是说一下再见这样 · Issue #588 · 78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32/issues/588)

服务器会在最后一条 AI 说话的内容之后大约一分钟的时候，给 AI 发一条消息：

```text
用户长时间没有说话，你可以简单告别后输出 `✿END✿` 结束本次对话。
```

这个在 MQTT + UDP 的场景下会有。WebSocket 不会。

## 三方开源服务端 xiaozhi-esp32-server

[xinnan-tech/xiaozhi-esp32-server: 本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server.](https://github.com/xinnan-tech/xiaozhi-esp32-server)

{% badge_github xinnan-tech xiaozhi-esp32-server release:true %}

[第十五章 告别在线平台：一步步搭建小智AI开源服务端，打通本地联调之路 - 知乎](https://zhuanlan.zhihu.com/p/1917995119191236926)
