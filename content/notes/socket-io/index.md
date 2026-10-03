---
title: Socket.IO
notebook: notes
tags:
  - it/websocket
date: 2024-05-23 23:57:34
updated: 2024-05-23 23:57:34
---
[Socket.IO](https://socket.io/)

[Introduction | Socket.IO](https://socket.io/docs/v4/)

{% badge_github socketio socket.io release:true %}

## 关于版本

- Socket.IO v2: released in May 2017 (major breaking changes)
- Socket.IO v3: released in November 2020 (major breaking changes)
- SOcket.IO v4: released in March 2021 (no protocol related breaking changes)

JS Socket.IO | Socket.IO protocol | Engine.IO protocol
---------|----------|---------
 0.9.x | 1, 2 | 1, 2
 1.x and 2.x | 3, 4 | 3
 3.x and 4.x | 5 | 4

其中 Engine.IO protocol version 就是建立连接时参数 `EIO` 的值。

比如 client version 如果是 2.x，EIO 就是 3；如果是 3.x 或 4.x，EIO 都是 4。在 postman 里可以选择 client version，查看发出去的请求参数。

## 微信小程序 + Go

服务端如果用 Go，可以选择目前官方推荐的 [googollee/go-socket.io](https://github.com/googollee/go-socket.io)，但目前支持 Socket.IO 2.x（Socket.IO protocol = 3，Engine.IO protocol = 3）。

[googollee/go-socket.io: socket.io library for golang, a realtime application framework.](https://github.com/googollee/go-socket.io)

{% badge_github googollee go-socket.io release:true %}

客户端如果是微信小程序，也可以选择官方列出来的 [weapp-socketio/weapp.socket.io](https://github.com/weapp-socketio/weapp.socket.io)，目前最新版本应该是相当于 Socket.IO 3.x（但也可以支持较低的 4.x 版本）。如果要跟 googollee/go-socket.io 搭配，需要使用 2.2.0 版本。

[weapp-socketio/weapp.socket.io: A WebSocket client for building WeChat Mini Program implement by socket.io](https://github.com/weapp-socketio/weapp.socket.io)

{% badge_github weapp-socketio weapp.socket.io release:true %}

## 二进制数据

抓包观测 event 中二进制数据的传输，客户端对不同数据类型的打包方式不太一样。

- Uint8Array

会序列化成 map，key 是数组下标（字符串格式），值是每一个数字，如 `"data":{"0":121,"1":117,"2":104,"3":117}`。

服务端收到的数据是 `map[0:121 1:117 2:104 3:117]`。

- Array

如果用 `Array.from(...)` 转换一下，客户端发送的就是数值数组，如 `"data":[121,117,104,117]`。

服务端收到的也是数组 `[121 117 104 117]`，可以直接赋值给 `[]byte` 类型的字段。

- Base64 string

如果用 base64 编码之后发送， 客户端发送的就是字符串，如 `"data":"eXVodQ=="`。

服务端收到的也是字符串 `eXVodQ==`，可以赋值给字符串字段，也可以直接赋值给 `[]byte` 字段，Go 会自动 decode。

服务端发送 `[]byte` 数据，会 encode 为 base64 字符串，客户端得到的就还是字符串，需要自己解码。
