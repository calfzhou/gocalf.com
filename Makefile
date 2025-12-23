PATH  := node_modules/.bin:$(PATH)
SHELL := /bin/bash

list:
	$(info Available targets:)
	$(info )
	@LC_ALL=C $(MAKE) -pRrq -f $(firstword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/(^|\n)# Files(\n|$$)/,/(^|\n)# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | grep -E -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	pnpm install

build:
	pnpm run build

generate: build

clean:
	pnpm run clean

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
	hexo new note -p "../notes/$(slug)/index.md" "$(title)"

post: check-slug-and-title
	hexo new post -p "$(shell date '+%Y')/$(slug)" "$(title)"

coding: check-slug-and-title
	hexo new coding -p "../coding/$(slug)/index.md" "$(title)"
	cp scaffolds/coding/* "source/coding/$(slug)/"

.PHONY: list install build generate clean server s note post coding
