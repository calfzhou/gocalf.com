<%*
let slug = tp.file.title;
let title = slug;
let folder = tp.file.folder(true);
if (slug.startsWith('Untitled')) {
  slug = await tp.system.prompt('Slug (lowercase letters, digits, internal hyphens):');
  if (!slug || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug)) throw new Error('Invalid or cancelled slug');
  title = await tp.system.prompt('Title:', slug.replace(/-/g, ' '));
  if (!title || !title.trim()) throw new Error('Title is required');
  const target = `coding/${slug}/index`;
  if (app.vault.getAbstractFileByPath(target) || app.vault.getAbstractFileByPath(target + '.md')) throw new Error('Destination already exists');
  await tp.file.move(target);
  folder = target.slice(0, target.lastIndexOf('/'));
}
// Copy text resources only; never execute them or overwrite an existing solution.
for (const name of ['solution.py', 'solution_test.py']) {
  const destination = `${folder}/${name}`;
  if (!app.vault.getAbstractFileByPath(destination)) {
    const text = await app.vault.adapter.read(`_templates/coding/${name}`);
    await app.vault.create(destination, text);
  }
}
%>---
title: <% JSON.stringify(title) %>
date: <% tp.file.creation_date('YYYY-MM-DDTHH:mm:ssZ') %>
lastmod: <% tp.file.creation_date('YYYY-MM-DDTHH:mm:ssZ') %>
draft: true
tags: []
---
<% tp.file.cursor() %>
## Problem

TODO: description and problem URL

**Example 1:**

> Input: TODO\
> Output: TODO

**Constraints:**

- TODO

## Test Cases

{{< snippet src="solution_test.py" >}}

## Thoughts

## Code

{{< snippet src="solution.py" >}}
