---
title: Git Cheats
notebook: notes
tags:
  - it/git
mermaid: true
date: 2025-12-28 15:21:24
updated: 2025-12-28 15:59:47
---
## Useful Aliases

Refer to [dotfiles/git/gitconfig at master · calfzhou/dotfiles](https://github.com/calfzhou/dotfiles/blob/master/git/gitconfig).

## Delete a Remote Branch

```bash
git push origin --delete BRANCH
```

## List Changed Files (w/o Details)

```bash
git diff --name-only BRANCH
git show --name-only COMMIT-ID
```

## List Commits Gap Between Two Branches

```bash
git l --left-right master...HEAD
# or
git log ---left-right --one-line --graph master...HEAD
```

Where a `>` commit is in the right (2nd) branch, while a `<` commit is in the left (1st) branch.

## Diff Two Arbitrary Files

```bash
git diff --no-index -- FILE1 FILE2
```

## See the Changes Made by a Commit to the Specified File

```bash
git show COMMIT-ID FILE
# or
git show --oneline COMMIT-ID FILE
```

Scenario: When `git l` a specific file, usually I'd like to see what changed in a history commit.

```shell-session
$ git l FILE
* db217ef84d3 2024-10-24 05:43 ...
* edfd91a00d1 2024-10-02 07:51 ...
* 01e00a9bc7e 2024-09-30 17:04 ...
```

I want to see the changes made to this file by commit db217ef84d3 (without looking at the changes to other files):

```bash
git show --oneline db217ef84d3 FILE
```

## Track Whether and How a Commit got into a Branch

To list branches containing the given commit:

```bash
git branch --contains COMMIT-ID
```

To track it:

```powershell
gitk COMMIT-ID..HEAD --ancestry-path
```

This will show only commits that are descendants of the commit `COMMIT-ID` and antecessors of the HEAD of current branch (you can use any two commits separated by `..`).

[github - Git track how a commit got into a branch - Stack Overflow](https://stackoverflow.com/questions/25750842/git-track-how-a-commit-got-into-a-branch)

## 撤回 Commit

### 撤回最后一次 Commit

```bash
git reset --hard HEAD~1
git push -f
```

### 撤回中间的某一次 Commit

比如：

```mermaid
gitGraph:
  commit id: "A"
  commit id: "B"
  commit id: "C"
  commit id: "D"
  commit id: "E"
```

要删掉 commit "C"：

```bash
git rebase --onto B C
```

## The `~` vs. The `^`

参考：[Git 中的 \~ 和 ^ - scarletsky](https://scarletsky.github.io/2016/12/29/tilde-and-caret-in-git/)

如果想要 `HEAD` 的第 10 个祖先，直接用 `HEAD~10` 就可以。`<rev>~<n>` 用来表示一个提交的第 n 个祖先提交，如果不指定 n，那么默认为 1。 另外，`HEAD~~~` 和 `HEAD~3` 等价。

`<rev>^<n>` 用来表示一个提交的第 n 个父提交，如果不指定 n，那么默认为 1。 和 `~` 不同的是，`HEAD^^^` 并不等价于 `HEAD^3`，而是等价与 `HEAD^1^1^1`。

`~` 获取第一个祖先提交，`^` 可以获取第一个父提交。 其实第一个祖先提交就是第一个父提交，反之亦然。 因此，当 n 为 1 时，`~` 和 `^` 其实是等价的。

> Here is an illustration, by Jon Loeliger. Both commit nodes B and C are parents of commit node A. Parent commits are ordered left-to-right.

```text
G   H   I   J
 \ /     \ /
  D   E   F
   \  |  / \
    \ | /   |
     \|/    |
      B     C
       \   /
        \ /
         A
A =      = A^0
B = A^   = A^1     = A~1
C = A^2  = A^2
D = A^^  = A^1^1   = A~2
E = B^2  = A^^2
F = B^3  = A^^3
G = A^^^ = A^1^1^1 = A~3
H = D^2  = B^^2    = A^^^2  = A~2^2
I = F^   = B^3^    = A^^3^
J = F^2  = B^3^2   = A^^3^2
```
