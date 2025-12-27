---
<%*
let slug = tp.file.title;
let title = slug;
if (slug.startsWith('Untitled')) {
  slug = await tp.system.prompt('Slug:');
  title = await tp.system.prompt('Title:', slug);
  await tp.file.rename(slug);
}
%>
title: <% title %>
type: story
date: <% tp.file.creation_date('') %>
updated: <% tp.file.last_modified_date('') %>
---
<% tp.file.cursor() %>
