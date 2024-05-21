---
title: Semantic Commit Message
notebook: notes
tags:
  - it/git
wiki: notes
menu_id: notes
date: 2024-05-21 19:36:09
updated: 2024-05-21 19:36:09
references:
  - '[Karma - Git Commit Msg](https://karma-runner.github.io/6.4/dev/git-commit-msg.html)'
---
## Git Commit Message Format

> In the repository we use and enforce the commit message conventions. The conventions are verified using [commitlint](https://conventional-changelog.github.io/commitlint/) with [Angular config](https://www.npmjs.com/package/@commitlint/config-angular).

{% badge_github conventional-changelog commitlint release:true %}

> commitlint checks if your commit messages meet the [conventional commit format](https://conventionalcommits.org/).

Format of the commit message:

``` text
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

Example commit message:

``` text
fix(middleware): ensure Range headers adhere more closely to RFC 2616

Add one new dependency, use `range-parser` (Express dependency) to compute
range. It is more well-tested in the wild.

Fixes #2310
```

## `type` Value

- **feat**: new feature for the user
- **fix**: bug fix for the user
- **perf**: performance improvements
- **docs**: changes to documentation
- **style**: formatting, missing semi colons, etc.
- **refactor**: refactoring production code, e.g. renaming a variable
- **test**: adding missing tests, refactoring tests; no production code change
- **chore**: updating build configuration, development tools or other changes irrelevant to the user
- **build**: build tooling, Docker configuration change
- **ci**: test runner, Github Actions workflow changes
- **revert**: changes that don't correspond to the above -- should be rare!

Example of `<type>: <subject>`:

``` yaml
feat: add beta sequence
fix: remove broken confirmation message
docs: explain hat wobble
style: convert tabs to spaces
refactor: share logic between 4d3d3d3 and flarhgunnstow
test: ensure Tayne retains clothing
chore: add Oyster build script
```

## `scope` Value

Example `<scope>` values:

- init
- runner
- watcher
- config
- web-server
- proxy

## Blog Site Specific Conventions

### Blog Site `type` Value

- **add**: 添加文章、笔记、文档
- **del**: 删除文章、笔记、文档
- **update**: 更新文章、笔记、文档，一般指有较大的内容变更或补充
- **fix**: 修复文章、笔记、文档中的错误，一般指修正一些错误
- **refine**: Refine 文章、笔记、文档，一般指微调

### Blog Site `scope` Value

Examples:

- posts/blahblah
- notes/blahblah
- foobar
