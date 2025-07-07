---
<%*
let title = tp.file.title
if (title.startsWith('Untitled')) {
  title = await tp.system.prompt('Slug:')
  await tp.file.rename(title)
}
%>
title: <% title %>
notebook: notes
tags: []
date: <% tp.file.creation_date('') %>
updated: <% tp.file.last_modified_date('') %>
---
<% tp.file.cursor() %>
