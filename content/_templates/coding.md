<%*
// Use only for a new, empty article in the content/ vault.
if (tp.file.content.trim()) throw new Error('This template requires an empty note; existing content and dates are not replaced');
const current = tp.file.path(true);
const name = tp.file.title;
const created = tp.file.creation_date('YYYY-MM-DDTHH:mm:ssZ');
const inBundle = /^coding\/[a-z0-9]+(?:-[a-z0-9]+)*\/index\.md$/.test(current);
if (name === '_index' || (name === 'index' && !inBundle)) {
  throw new Error('Collection roots are not articles; use a slug or a bundle index.md');
}
if (!inBundle && app.vault.getAbstractFileByPath(`${tp.file.folder(true)}/index.md`)) {
  throw new Error('This folder already contains a leaf bundle; do not create a second article inside it');
}
const untitled = /^(?:Untitled|未命名)(?: \d+)?$/i.test(name);
let slug = inBundle ? tp.file.folder(true).split('/').pop() : name;
if (untitled || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug)) {
  slug = await tp.system.prompt('Slug (lowercase letters, digits, internal hyphens):');
}
if (!slug || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug)) throw new Error('Invalid or cancelled slug');
const suggestedTitle = untitled || inBundle || name === slug ? slug.replace(/-/g, ' ') : name;
const title = await tp.system.prompt('Title:', suggestedTitle);
if (!title || !title.trim()) throw new Error('Title is required');
const folder = inBundle ? tp.file.folder(true) : `coding/${slug}`;
const target = `${folder}/index.md`;
if (target !== current && (app.vault.getAbstractFileByPath(folder) || app.vault.getAbstractFileByPath(target))) {
  throw new Error('Destination already exists; nothing overwritten');
}
// Read all needed template resources before moving; never execute Python.
const companions = new Map();
for (const name of ['solution.py', 'solution_test.py']) {
  const path = `${folder}/${name}`;
  const existing = app.vault.getAbstractFileByPath(path);
  if (existing?.children) throw new Error(`Companion path is a folder: ${path}`);
  if (!existing) companions.set(path, await app.vault.adapter.read(`_templates/coding/${name}`));
}
if (target !== current) await tp.file.move(target.slice(0, -3));
for (const [path, text] of companions) {
  if (!app.vault.getAbstractFileByPath(path)) await app.vault.create(path, text);
}
%>---
title: <% JSON.stringify(title) %>
date: <% created %>
lastmod: <% created %>
draft: true
tags: []
---
<% tp.file.cursor() %>
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

{{< snippet src="solution_test.py" >}}

## Thoughts

## Code

{{< snippet src="solution.py" >}}
