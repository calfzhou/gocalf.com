---
title: Linux Server Setup
notebook: notes
tags:
  - software/linux
  - it/server
date: 2025-12-21 12:31:54
updated: 2026-04-04 11:48:25
---
## Ubuntu

Version: Ubuntu 24.04 LTS

### Linode Specific

```bash
# New user: calf:admin
groupadd admin
useradd -g admin calf
chsh -s /bin/bash calf
mkhomedir_helper calf
chmod +w /etc/sudoers
vim /etc/sudoers
# add a line:
# calf    ALL=(ALL)       NOPASSWD: ALL
chmod -w /etc/sudoers

# Setup ssh-key
su - calf
pwd
# /home/calf
ssh-keygen -t ed25519
vim .ssh/authorized_keys
# add local machine's pub key into this file, then save
chmod 644 .ssh/authorized_keys

# Disable password login, disable root login
sudo vim /etc/ssh/sshd_config
# make sure these settings:
# PasswordAuthentication no
# PermitRootLogin no
# KbdInteractiveAuthentication no
sudo sshd -t
sudo service ssh reload
```

### Azure Specific

By default, the root user is not allowed to log in via SSH.

In case if really needed, modify `.ssh/authorized_keys`, comment out the following line then add public key:

```text
no-port-forwarding,no-agent-forwarding,no-X11-forwarding,command="echo 'Please login as the user \"calf\" rather than the user \"root\".';echo;sleep 10;exit 142" ssh-ed25519 ......
```

### Aliyun Specific

The default user is `ecs-user`.

To access some "not-exist" websites:

```bash
ssh -C -f -D 1080 -N calf@THANK-GOD
export all_proxy=socks5://127.0.0.1:1080

# curl, or something else

unset all_proxy
```

### Change the Hostname

```bash
sudo hostname DESIRED-NAME
```

### Change the Timezone

```bash
sudo timedatectl set-timezone Asia/Shanghai
```

> [!tip]
> Azure server's default time zone is UTC.

### Test Network Speed

Run on local machine:

```shell-session
$ dd if=/dev/urandom of=128mb.bin bs=32M count=4 iflag=fullblock
4+0 records in
4+0 records out
134217728 bytes (134 MB, 128 MiB) copied, 0.43566 s, 308 MB/s

$ scp 128mb.bin THE-SERVER:
128mb.bin                                            100%  128MB   5.9MB/s   00:21

$ scp THE-SERVER:128mb.bin .
128mb.bin                                            100%  128MB   8.8MB/s   00:14
```

### Install Docker

[Install Docker Engine on Ubuntu | Docker Docs](https://docs.docker.com/engine/install/ubuntu/)

```bash
sudo apt-get update

# Add Docker's official GPG key:
# sudo apt-get install ca-certificates
#> ca-certificates is already the newest version (20240203).
# sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# To install the latest version of docker.
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

docker --version
#> Docker version 28.3.0, build 38b7060
docker compose version
#> Docker Compose version v2.37.3

service docker status
```

To allow non-privileged users to run Docker commands:

```bash
sudo usermod -aG docker USER

# Log out and log back in so that your group membership is re-evaluated.
# Try `docker ps` without `sudo`.
docker ps
#> CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Install Docker on Aliyun

[在 Linux 系统上安装和使用 Docker 和 Docker Compose - 云服务器 ECS - 阿里云](https://help.aliyun.com/zh/ecs/user-guide/install-and-use-docker#8dca4cfa3dn0e)

```bash
sudo apt-get update

# Use Aliyun's mirror
sudo curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
sudo add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update

# ...
```

配置镜像：

```bash
sudo tee /etc/docker/daemon.json <<-'EOF'
{
    "registry-mirrors": [
        "https://dockerproxy.com",
        "https://mirror.baidubce.com",
        "https://docker.nju.edu.cn"
    ]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

docker info
#> ...
#> Registry Mirrors:
#>   ...
```

> [!caution]
> 上述镜像源不一定可用，更多镜像参见 [境内 Docker 镜像状态监控](https://status.anye.xyz/)。

### Install Tailscale

[Tailscale | Secure Connectivity for AI, IoT & Multi-Cloud](https://tailscale.com/)

```bash
curl -fsSL https://tailscale.com/install.sh | sh

sudo tailscale up
# To authenticate, visit: ...
```

## Service Deployment Setup

### The First Time Setup

> [!note]
>
> ```bash
> sudo su -
> ```

```bash
ssh-keygen -t ed25519
```

Add the public key to "Deploy keys" of the deployment GitHub repo: `https://github.com/USER/REPO/settings/keys`.

```bash
cd /opt
mkdir SERVICE-ROOT
cd SERVICE-ROOT

git clone git@github.com:USER/REPO.git deploy

ln -s deploy/SERVER-NAME/services .

# or

mkdir services
cd services
ln -s ../deploy/DESIRED-SERVICE .
```

### Regular Update

```bash
cd /opt/SERVICE-ROOT/deploy
git pull

cd /opt/SERVICE-ROOT/services/DESIRED-SERVICE
# Follow the service README file to update.
```

## Anbolt Linux 盒子 + Ubuntu

瑞芯微主控 RK3528

[Anbolt 电视盒媒体播放器安卓 Linux – Anbolt Armbox World](https://anbolt.net/)

> [!warning]
> Don't run `upgrade`!

### Info

```text
 __  _____  ___ ___ ___  ___  _ ____
 \ \/ ( _ )( _ ) _ \ _ \/ _ \/ |__ /
  >  </ _ \/ _ \  _/   / (_) | ||_ \
 /_/\_\___/\___/_| |_|_\___/|_|___/

 v25.05 rolling for X88pro13 running Armbian Linux 6.1.99-vendor-rk35xx

 Packages:     Ubuntu stable (jammy), possible distro upgrade (noble)
 Updates:      Kernel upgrade enabled and 92 packages available for upgrade
 Support:      DIY (custom image)

 Commands:

 Configuration : armbian-config
 Upgrade       : armbian-upgrade
 Monitoring    : htop
```

### Change Locale

```bash
update-locale LANG=en_US.UTF-8
update-locale LC_MESSAGES=en_US.UTF-8
update-locale LANGUAGE=en_US:en
```

### Expand EMMC to Root FS

```bash expand_emmc_rootfs.sh
#!/bin/bash
EMMC_ROOT=$(mount -l | grep "on / type" | cut -d ' ' -f 1)
echo "are you sure resize ${EMMC_ROOT}? (y/n)"
read answer
if [[ $answer =~ ^[Yy]$ ]]; then
    EMMC_ROOT_DISK=$(echo $EMMC_ROOT | cut -c 1-12)
    parted $EMMC_ROOT_DISK resizepart 2 100%
    echo "start resize emmc..."
    resize2fs ${EMMC_ROOT}
    sync
    echo "resize finished"
elif [[ $answer =~ ^[Nn]$ ]]; then
    exit
fi
```

```shell-session
# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk1p2  6.9G  1.3G  5.5G  20% /

# lsblk
NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
mmcblk1      179:0    0 58.2G  0 disk
├─mmcblk1p1  179:1    0  256M  0 part /boot
└─mmcblk1p2  179:2    0  7.1G  0 part /var/log.hdd
                                      /

# ./expand_emmc_rootfs.sh
are you sure resize /dev/mmcblk1p2? (y/n)
y
Warning: Not all of the space available to /dev/mmcblk1 appears to be used, you can fix the GPT to use all of the space (an extra 106414080 blocks) or continue with the
current setting?
Fix/Ignore? f
Partition number? 2
Warning: Partition /dev/mmcblk1p2 is being used. Are you sure you want to continue?
Yes/No? y
End?  [7885MB]? 100%
Information: You may need to update /etc/fstab.

start resize emmc...
resize2fs 1.46.5 (30-Dec-2021)
Filesystem at /dev/mmcblk1p2 is mounted on /; on-line resizing required
old_desc_blocks = 1, new_desc_blocks = 8
The filesystem on /dev/mmcblk1p2 is now 15198203 (4k) blocks long.

resize finished

# lsblk
NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
mmcblk1      179:0    0 58.2G  0 disk
├─mmcblk1p1  179:1    0  256M  0 part /boot
└─mmcblk1p2  179:2    0   58G  0 part /var/log.hdd
                                      /

# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk1p2   58G  1.3G   56G   3% /
```

### Install Docker

```bash
apt update
apt install -y apparmor-utils docker.io docker-compose
# Note: there is no docker-compose-plugin

docker --version
#> Docker version 28.2.2, build 28.2.2-0ubuntu1~22.04.1
docker-compose version
#> docker-compose version 1.29.2, build unknown
#> docker-py version: 5.0.3
#> CPython version: 3.10.12
#> OpenSSL version: OpenSSL 3.0.2 15 Mar 2022

service docker status
```
