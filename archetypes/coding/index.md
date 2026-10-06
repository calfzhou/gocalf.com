---
title: {{ (or (os.Getenv "HUGO_NEW_TITLE") (replace .Name "-" " ")) | jsonify }}
date: {{ .Date }}
lastmod: {{ .Date }}
draft: true
tags: []
---

## Problem

TODO

TODO: problem URL

**Example 1:**

> Input: TODO\
> Output: TODO

**Example 2:**

> Input: TODO\
> Output: TODO

**Example 3:**

> Input: TODO\
> Output: TODO

**Constraints:**

- TODO
- TODO

## Test Cases

``` python
TODO: default code definition
```

{{ `{{< snippet src="solution_test.py" >}}` }}

## Thoughts

## Code

{{ `{{< snippet src="solution.py" >}}` }}
