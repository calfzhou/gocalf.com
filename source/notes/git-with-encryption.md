---
title: Git with Encryption
wiki: notes
menu_id: notes
date: 2024-04-20 21:16:54
updated: 2024-04-21 11:46:47
---
## git-remote-gcrypt

[git-remote-gcrypt - PGP-encrypted git remotes](https://spwhitton.name/tech/code/git-remote-gcrypt/)

{% badge_github spwhitton git-remote-gcrypt %}

> git-remote-gcrypt is a git remote helper to push and pull from repositories encrypted with [GnuPG](https://www.gnupg.org/), using a custom format. This remote helper handles URIs prefixed with `gcrypt::`.

{% box color:yellow %}
This tool only does *REMOTE* encryption. The *LOCAL* repository is *NOT* encrypted.
{% endbox %}

### 本地已有仓库推送到远程

需要本地先准备好 [PGP key pair](/notes/pgp)，应该有 E 用途和 S 用途的子密钥各一个分别用来加密和签名。

``` bash
brew install git-remote-gcrypt

# Go to a git repository, then:
git remote add cryptremote gcrypt::git@github.com:<user>/<repo>.git # or any arbitrary remote name

git config remote.cryptremote.gcrypt-participants "UID/KEY-ID UID/KEY-ID"
git config gcrypt.require-explicit-force-push true # 不是必须，但推荐，以确保 push 的时候一定加上 --force 参数

# 避免 global 配置中的信息干扰（按需进行）
git config user.signingkey ''
git config commit.gpgsign false

git push -u cryptremote master --force
# or
git push --all cryptremote --force

# If failed with error: gpg: signing failed: Inappropriate ioctl for device
export GPG_TTY=$(tty)
# Might need `git remote remove cryptremote` and add the remote back again.
```

git-remote-gcrypt 可以用的 backend：

- `gcrypt::git@github.com:<user>/<repo>.git`
- `gcrypt::/path/to/local/folder`
  - 会直接创建目标目录，但创建出来的目录并不是一个 git (bare) repo，只是 plain files（不影响以后借助 gcrypt clone 回来）
- `gcrypt::rsync://<host>/<path>`

当需要重新从远程 clone 时，直接 `git clone gcrypt::<remote-url>` 即可。

### 从加密的远程仓库 clone 到本地

可以直接 clone，或者添加 remote 之后 fetch / pull。跟普通的 remote 没有太大区别，除了协议要用 `gcrypt::`，以及注意相关的 config。

``` bash
git clone gcrypt::remote-url-or-path local-repo
cd local-repo

git config remote.cryptremote.gcrypt-participants "UID/KEY-ID UID/KEY-ID"
git config gcrypt.require-explicit-force-push true # 不是必须，但推荐，以确保 push 的时候一定加上 --force 参数

# 避免 global 配置中的信息干扰（按需进行）
git config user.signingkey ''
git config commit.gpgsign false
```

## git-crypt

[git-crypt - transparent file encryption in git](https://www.agwa.name/projects/git-crypt/)

{% badge_github AGWA git-crypt release:true %}

> **git-crypt** enables transparent encryption and decryption of files in a git repository. Files which you choose to protect are encrypted when committed, and decrypted when checked out. git-crypt lets you freely share a repository containing a mix of public and private content. git-crypt gracefully degrades, so developers without the secret key can still clone and commit to a repository with encrypted files. This lets you store your secret material (such as keys or passwords) in the same repository as your code, without requiring you to lock down your entire repository.

``` bash
brew install git-crypt
```

用 C++ 写的一个工具，还没有具体用过。和 git-remote-gcrypt 相比的优势是可以只加密仓库中的一部分文件。

## git-encrypt

{% note DEPRECATED! 此项目 2014 年之后就不在维护了。Since Sept. 2023, it is actually not working anymore with newer openssl on MacOS. color:error %}

[shadowhand/git-encrypt at legacy](https://github.com/shadowhand/git-encrypt/tree/legacy)

{% badge_github shadowhand git-encrypt release:true %}

{% badge_github calfzhou git-encrypt %}

``` bash
# Cannot be installed by brew.

git clone git@github.com:calfzhou/git-encrypt.git
# Add to $PATH

# Go to a git repository.
gitcrypt init
```
