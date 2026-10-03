# GoCalf

## Build and preview

Use Hugo **0.166.0 extended** directly. The legacy Makefile/package scripts below
run Hexo; package installation is not required for Hugo.

```sh
# Choose a free port; stop the preview with Ctrl-C.
hugo server --bind 127.0.0.1 --port 14740 --disableFastRender

# Build into a fresh directory without interfering with an existing preview lock.
run=$(mktemp -d "$PWD/var/hugo-build-XXXXXX")
hugo --destination "$run/public" --cacheDir "$run/cache" --noBuildLock --panicOnWarning
```

## Markdown authoring

Use **YAML `---` front matter** and preserve authored publication/update dates.
Ordinary headings use native Hugo IDs. Coding example fields use explicit backslash
hard breaks where separate lines are intended. Image attributes follow native
standalone/quoted-block placement.

## Historical Hexo workflow (not Hugo)

## Setup

``` bash
make install
```

## Preview

``` bash
make s
```

## Debugging Theme

Clone hexo-theme-stellar at `themes/stellar`.

## Writing

### Notes

To create a new note, use `make note`, e.g.:

``` bash
make note slug=new-note title='New Note'
```
