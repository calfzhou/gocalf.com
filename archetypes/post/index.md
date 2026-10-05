---
title: {{ (or (os.Getenv "HUGO_NEW_TITLE") (replace .Name "-" " ")) | jsonify }}
date: {{ .Date }}
lastmod: {{ .Date }}
draft: true
type: story
---
