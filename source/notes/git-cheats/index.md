---
title: Git Cheats
notebook: notes
tags:
  - it/git
date: 2025-12-28 15:21:24
updated: 2025-12-28 15:21:24
---
## Useful Aliases

Refer to [dotfiles/git/gitconfig at master · calfzhou/dotfiles](https://github.com/calfzhou/dotfiles/blob/master/git/gitconfig).

## Delete a Remote Branch

``` bash
git push origin --delete BRANCH
```

## List Changed Files (w/o Details)

``` bash
git diff --name-only BRANCH
git show --name-only COMMIT-ID
```

## List Commits Gap Between Two Branches

``` bash
git l --left-right master...HEAD
# or
git log ---left-right --one-line --graph master...HEAD
```

Where a `>` commit is in the right (2nd) branch, while a `<` commit is in the left (1st) branch.

## Diff Two Arbitrary Files

``` bash
git diff --no-index -- FILE1 FILE2
```

## See the Changes Made by a Commit to the Specified File

``` bash
git show COMMIT-ID FILE
# or
git show --oneline COMMIT-ID FILE
```

Scenario: When `git l` a specific file, usually I'd like to see what changed in a history commit.

``` shell-session
$ git l FILE
* db217ef84d3 2024-10-24 05:43 ...
* edfd91a00d1 2024-10-02 07:51 ...
* 01e00a9bc7e 2024-09-30 17:04 ...
```

I want to see the changes made to this file by commit db217ef84d3 (without looking at the changes to other files):

``` bash
git show --oneline db217ef84d3 FILE
```

## Track Whether and How a Commit got into a Branch

To list branches containing the given commit:

``` bash
git branch --contains COMMIT-ID
```

To track it:

``` powershell
gitk COMMIT-ID..HEAD --ancestry-path
```

This will show only commits that are descendants of the commit `COMMIT-ID` and antecessors of the HEAD of current branch (you can use any two commits separated by `..`).

[github - Git track how a commit got into a branch - Stack Overflow](https://stackoverflow.com/questions/25750842/git-track-how-a-commit-got-into-a-branch)
