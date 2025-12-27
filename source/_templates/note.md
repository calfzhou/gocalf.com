---
<%*
let slug = tp.file.title;
let title = slug;
if (slug.startsWith('Untitled')) {
  slug = await tp.system.prompt('Slug:');
  title = await tp.system.prompt('Title:', slug);
  await tp.file.move(`/notes/${slug}/index`);
}
%>
title: <% title %>
notebook: notes
tags: []
date: <% tp.file.creation_date('YYYY-MM-DD HH:mm:SS') %>
updated: <% tp.file.last_modified_date('YYYY-MM-DD HH:mm:SS') %>
---
<% tp.file.cursor() %>
