---
title: Python Package Management
notebook: notes
updated: 2025-11-17 22:21:03
date: 2025-11-17 22:21:03
tags:
  - it/python
references:
  - '[Python package dependency management - pip freeze - requirements.txt and constraints.txt](https://code-maven.com/python-package-dependency-management)'
---
## Version and Virtual Environment

[Python Version Management & Virtual Environments](../python-version-management-virtual-environments/index.md)

## Package Management

[Python package dependency management - pip freeze - requirements.txt and constraints.txt](https://code-maven.com/python-package-dependency-management)

TL;DR

> Keep the list of immediate dependencies in **requirements.txt** without declaring version numbers.
> Keep the output of **pip freeze** with the specific version numbers in **constraints.txt**.

### Adding new packages

As we need new python packages add their names to the requirements.txt file without any restriction and run

```bash
pip install -r requirements.txt -c constraints.txt
```

Verify that the new package works as needed. (Run your own tests). Then run

```bash
pip freeze > constraints.txt
```

Then commit both **requirements.txt** and **constraints.txt** to your version control system.

### Fresh installations

Later, any time you want to install packages to a fresh installation use

```bash
pip install -r requirements.txt -c constraints.txt
```

### Require specific version of a package

If your application requires a specific version of a package add that information to the requirements.txt file.

```text
package-name==SPECIFIC_VERSION
```

### Upgrade a package

If later you need to upgrade one of your immediate dependencies because you need some feature that only in a newer version exist then add this information as a minimum requirement to the requirements.txt file: **package>=SOME_VERSION**

### Removing required packages

We can simply remove the package from the requirements.txt file. The fact that it and its dependencies are listed in the constraints.txt file does not matter. They won't be installed. The only problem is that now we might have some lines in the constraints.txt file that are not relevant any more and that might impact a later installation. If you do the regular maintenance as described below then this will be cleaned up the next time you do it.

### Regular maintenance

You can do all the upgrades all at once, or you can cherry-pick.

For the former run:

```bash
pip install --upgrade -r requirements.txt
```

That will try to upgrade all of your dependencies to the latest.

You can upgrade a specific package:

```bash
pip install --upgrade PACKAGE
```

You can also remove some or all of the entries from the **constraints.txt file** and then run:

```bash
pip install --upgrade -r requirements.txt -c constraints.txt
```
