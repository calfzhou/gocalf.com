<%*
let slug = tp.file.title;
let title = slug;
if (slug.startsWith('Untitled')) {
  slug = await tp.system.prompt('Slug (lowercase letters, digits, internal hyphens):');
  if (!slug || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug)) throw new Error('Invalid or cancelled slug');
  title = await tp.system.prompt('Title:', slug.replace(/-/g, ' '));
  if (!title || !title.trim()) throw new Error('Title is required');
  const target = `blog/${tp.date.now("YYYY")}/${slug}/index`;
  if (app.vault.getAbstractFileByPath(target) || app.vault.getAbstractFileByPath(target + '.md')) throw new Error('Destination already exists');
  await tp.file.move(target);
}
%>---
title: <% JSON.stringify(title) %>
date: <% tp.file.creation_date('YYYY-MM-DDTHH:mm:ssZ') %>
lastmod: <% tp.file.creation_date('YYYY-MM-DDTHH:mm:ssZ') %>
draft: true
type: story
---
<% tp.file.cursor() %>
