# GoCalf

## Hugo migration pilot (local branch)

This branch currently publishes **16 pilot articles**, not the whole historical site.
Remaining original material stays under `source/`, outside Hugo content. Use Hugo
**0.166.0 extended** directly; the legacy Makefile/package scripts below still run Hexo.
Do not install/prepare packages for this Hugo preview.

```sh
# Run from gocalf.com-hugo; choose another port if already occupied.
hugo server --bind 127.0.0.1 --port 14740 --disableFastRender

# Strict static build into a fresh isolated destination:
run=$(mktemp -d "$PWD/var/hugo-build-XXXXXX")
hugo --destination "$run/public" --cacheDir "$run/cache" --panicOnWarning
```

Stop your preview with Ctrl-C. The pinned HTTPS Sidera submodule is already initialized.
Never target the preserved sibling `gocalf.com-public-hexo` as a build destination.
New/migrated Markdown uses **YAML `---` front matter**; normal headings need no manual
ID attributes. Hugo's default heading IDs are accepted; use explicit IDs only for a
specific reviewed compatibility need. Keep authored dates; conversion is not publishing.

Known pilot review blocker: the Mermaid graph in **PGP - Pretty Good Privacy** currently
falls back to source because of malformed multiline-label SVG from the shared renderer.
A strict static build succeeds; that alone is not full interactive/parity acceptance.
Giscus is explicitly off; edit links/Jinrishici remain deferred. No deployment/site push.
See the coordination repository's P4-B report for current evidence and remaining work.

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
