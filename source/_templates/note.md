---
<%*
let slug = tp.file.title
if (slug.startsWith('Untitled')) {
  slug = await tp.system.prompt('Slug:')
  title = await tp.system.prompt('Title:', slug)
  await tp.file.rename(slug)
}
%>
title: <% title %>
notebook: notes
tags: []
date: <% tp.file.creation_date('') %>
updated: <% tp.file.last_modified_date('') %>
---
<% tp.file.cursor() %>
