---
<%*
let slug = tp.file.title;
let title = slug;
if (slug.startsWith('Untitled')) {
  slug = await tp.system.prompt('Slug:');
  title = slug.split('-').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(' ');
  title = await tp.system.prompt('Title:', title);
  await tp.file.move(`/coding/${slug}/index`);
}
%>
title: <% title %>
notebook: coding
tags: []
date: <% tp.file.creation_date('YYYY-MM-DD HH:mm:SS') %>
updated: <% tp.file.last_modified_date('YYYY-MM-DD HH:mm:SS') %>
katex: false
---
## Problem

<% tp.file.cursor() %>TODO

<https://todo>

**Example 1:**

> Input: TODO
> Output: TODO

**Example 2:**

> Input: TODO
> Output: TODO

**Example 3:**

> Input: TODO
> Output: TODO

**Constraints:**

- TODO
- TODO

## Test Cases

```python
TODO: default code definition
```

{% asset_code solution_test.py %}

## Thoughts

## Code

{% asset_code solution.py %}
