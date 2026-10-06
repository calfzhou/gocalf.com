SHELL := /bin/sh
.DEFAULT_GOAL := help

# Pass author input through the environment, never interpolate it into shell code.
override slug := $(value slug)
override title := $(value title)
export slug title
port ?= 14740
export port

.PHONY: help list build serve server preview note post coding page draft
help list:
	@printf '%s\n' 'make build                 Production build (no drafts/future/expired)' 'make serve [port=14740]     Published-content preview' 'make preview [port=14740]   Include drafts and future content' 'make note|post|coding|page|draft slug=slug title="Title"' 'No install, clean, push or deployment targets.'

build:
	hugo --environment production --buildDrafts=false --buildFuture=false --buildExpired=false --panicOnWarning

serve server:
	hugo server --bind 127.0.0.1 --port "$$port" --disableFastRender

preview:
	hugo server --bind 127.0.0.1 --port "$$port" --disableFastRender --buildDrafts --buildFuture

note post coding page draft:
	@sh scripts/new-content.sh $@
