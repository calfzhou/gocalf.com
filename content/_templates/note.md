<%*
// Use only for a new, empty article in the content/ vault.
if (tp.file.content.trim()) throw new Error('This template requires an empty note; existing content and dates are not replaced');
const current = tp.file.path(true);
const name = tp.file.title;
const created = tp.file.creation_date('YYYY-MM-DDTHH:mm:ssZ');
const inBundle = /^notes\/[a-z0-9]+(?:-[a-z0-9]+)*\/index\.md$/.test(current);
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
const folder = inBundle ? tp.file.folder(true) : `notes/${slug}`;
const target = `${folder}/index.md`;
if (target !== current && (app.vault.getAbstractFileByPath(folder) || app.vault.getAbstractFileByPath(target))) {
  throw new Error('Destination already exists; nothing overwritten');
}
if (target !== current) await tp.file.move(target.slice(0, -3));
%>---
title: <% JSON.stringify(title) %>
date: <% created %>
lastmod: <% created %>
draft: true
tags: []
---
<% tp.file.cursor() %>
