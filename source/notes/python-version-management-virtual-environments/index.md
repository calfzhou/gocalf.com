---
title: Python Version Management & Virtual Environments
notebook: notes
updated: 2025-11-17 22:21:03
date: 2025-11-17 22:21:03
tags:
  - it/python
references:
  - '[Managing Multiple Python Versions With pyenv – Real Python](https://realpython.com/intro-to-pyenv/#working-with-multiple-environments)'
---
## Python Version Management - pyenv

{% badge_github pyenv pyenv release:true %}

> pyenv lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

What pyenv does...

- Lets you **change the global Python version** on a per-user basis (`pyenv global`).
- Provides support for **per-project Python versions** (`pyenv local`).
- Allows you to **override the Python version** with an environment variable (`pyenv shell`).
- Searches for commands from **multiple versions of Python at a time**. This may be helpful to test across Python versions with [tox](https://pypi.python.org/pypi/tox) .

In contrast with [pythonbrew](https://github.com/utahta/pythonbrew) (no longer under active development) and [pythonz](https://github.com/saghul/pythonz), pyenv does not...

- **Depend on Python itself.** pyenv was made from pure shell scripts. There is no bootstrap problem of Python.
- **Need to be loaded into your shell.** Instead, pyenv's shim approach works by adding a directory to your PATH.
- **Manage virtualenv.** Of course, you can create [virtualenv](https://pypi.python.org/pypi/virtualenv) yourself, or [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to automate the process.

### Installation

``` bash
brew install pyenv
```

Then follow the rest of the post-installation steps, starting with [Set up your shell environment for Pyenv](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv).

Add the following to `.zshrc`:

``` bash
export PYENV_ROOT="$HOME/.pyenv"
eval "$(pyenv init -)"
# eval "$(pyenv init --path)"
```

`pyenv` needs to be upgraded to install new Python versions:

``` bash
brew upgrade pyenv
pyenv install --list
```

### Usage

If `BUILD FAILED` on Mac OS when `pyenv install x.y.z`:

``` bash
sudo rm -rf /Library/Developer/CommandLineTools
xcode-select --install
pyenv install x.y.z
```

To select a pyenv-installed Python as the version to use, run one of the following commands:

- [`pyenv shell <version>`](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-shell) -- select just for current shell session（在环境变量 `PYENV_VERSION` 中设置指定的 version）
- [`pyenv local <version>`](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-local) -- automatically select whenever you are in the current directory (or its subdirectories)（在当前目录创建一个 `.python-version` 文件，记录指定的 version）
- [`pyenv global <version>`](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-shell) -- select globally for your user account（在 `$PYENV_ROOT` 目录中创建一个 `version` 文件，记录指定的 version）

### Plugins

[Plugins · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki/Plugins)

除了 pyenv-virtualenv，没什么特别需要的。

## Virtual Environments Management - pyenv-virtualenv

{% badge_github pyenv pyenv-virtualenv release:true %}

> pyenv-virtualenv is a [pyenv](https://github.com/pyenv/pyenv) plugin that provides features to manage virtualenvs and conda environments for Python on UNIX-like systems.

> [!note]
> `pyenv-veirtualenv` is preferred rather than `pyenv-virtualenvwrapper`

``` bash
# 2022-08-04 10:37 The last release (v1.1.5) was on Feb 14, 2019
brew install --HEAD pyenv-virtualenv
# Or simply clone plugin code into pyenv plugins folder:
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```

Zsh has a [pyenv](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/pyenv) plugin, which also loads pyenv-virtualenv if exists.

``` bash
# Create virtualenv
pyenv virtualenv <name>
pyenv virtualenv 2.7.10 <name>

# Activate virtualenv
pyenv activate <name>
pyenv deactivate

# Delete existing virtualenv
pyenv uninstall <name>
# or
pyenv virtualenv-delete <name>
```

Virtualenvs can also be used by `pyenv local`, `pyenv shell`, or `pyenv global` if necessary.

### Automatically Activate/Deactivate Virtualenvs

pyenv 虽然通过 `pyenv local` （即 `.python-version` 文件）也可以实现进入一个目录时自动切换到指定的 python 版本（支持多个版本、支持 virtualenv），但到目前（v2.3.2）仍然要求所指定的每一个版本必须存在，否则无法成功运行 python。虽然自动了，但过于强制。期望的是进入目录时，如果指定的版本（或 virtualenv）存在就自动切换，不存在就不切换。

pyenv-virtualenv 也说支持 auto activate，但也是基于 `.python-version` 文件，不知道跟 pyenv 自身的自动切换版本有什么区别（似乎是 pyenv-virtualenv 会额外 [activate the virtualenv](https://github.com/pyenv/pyenv-virtualenv/issues/368#issuecomment-749501149)），但实际效果也是如果指定 virtualenv 不存在，就无法运行 python（这个是 pyenv 控制的）。

还没找到现成的工具或插件（for zsh or pyenv）。

考虑仿照 zsh virtualenvwrapper 插件里的逻辑，实现一个类似的基于 pyenv-virtualenv 的自动切换函数，可以不用额外的配置文件，自动找与目录同名的 virtualenv，如果有就 activate，没有就算了。

## Package Management

[Python Package Management](python-package-management.md)
