PATH  := node_modules/.bin:$(PATH)
SHELL := /bin/bash

ls:
	ls

install:
	pnpm install

build:
	pnpm run build

server:
	pnpm run server

s: server

slug :=
title :=

check-slug-and-title:
ifndef slug
	$(error slug is not set, use `make note slug=slug title=title`)
endif
ifndef title
	$(error title is not set, use `make note slug=slug title=title`)
endif

note: check-slug-and-title
	hexo new note -p "../notes/$(slug)" "$(title)"

post: check-slug-and-title
	hexo new post -p "$(shell date '+%Y')/$(slug)" "$(title)"

.PHONY: ls install build server s note post
