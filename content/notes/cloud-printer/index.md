---
title: 云打印机
notebook: notes
tags:
  - software
  - hardware
date: 2026-04-04 20:34:29
updated: 2026-04-05 22:52:52
---
## 远程打印助手（互维云）

一款基于 [CUPS](https://www.cups.org/) 的微信小程序云打印服务，让普通打印机支持远程打印。

![互维云印](20260404-180619.png)

Docker image: [tzishue/cloud-printer - Docker Image](https://hub.docker.com/r/tzishue/cloud-printer)

> 可以用 [Linux Server Setup](../linux-server-setup/index.md) 中的 Anbolt 机顶盒（刷了 Ubuntu）跑这个服务。

```bash
# macOS
docker run -d \
  --name cloud-printer \
  -p 631:631 \
  -e TZ=Asia/Shanghai \
  -e CUPS_ADMIN_PASSWORD=admin123 \
  -v ./cloud-printer-cups:/etc/cups \
  -v ./cloud-printer-logs:/var/log/printer-client \
  -v ./cloud-printer-device-id:/etc/printer-device-id-vol \
  --privileged \
  --restart unless-stopped \
  tzishue/cloud-printer:latest
```

> Or `-p 1631:631` if port 631 is already used by local CUPS server.

```yaml docker-compose.yml
services:
  cloud-printer:
    container_name: cloud-printer
    image: tzishue/cloud-printer:latest
    ports:
      - "631:631"
    environment:
      TZ: Asia/Shanghai
      CUPS_ADMIN_PASSWORD: admin123
    volumes:
      - ./data/cups:/etc/cups
      - ./data/logs:/var/log/printer-client
      - ./data/device-id:/etc/printer-device-id-vol
    privileged: true
    restart: unless-stopped
```

访问 <http://127.0.0.1:631/> or <http://127.0.0.1:1631/>，管理后台登录用户名 `root`，密码为 `admin123`（可通过环境变量 `CUPS_ADMIN_PASSWORD` 修改）。添加打印机，测试没问题即可使用微信小程序远程打印了。

## Cannon imageCLASS MF641Cw

在 CUPS 添加打印机，选「Internet Printing Protocol (ipp)」。

Connection: `ipp://<PRINTER-IP>:631/ipp/print`。

手动指定 PPD 文件：[mf641c mf641cw PPD file](https://gist.github.com/calfzhou/5e8cc1365d9a6a1a4ef4fe082efddf3f)。
