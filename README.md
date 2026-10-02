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

The pilot's Mermaid multiline-label issue is fixed in pinned Sidera **c45210b**:
original diagram sources render as XML-safe SVG text without a library/sandbox change.
Strict native and bounded interactive checks cover all 16 articles and the used cube/
diagram/search/source-copy features; user P4-B review is still required, not full-site
or production parity acceptance. Giscus is explicitly off; edit links/Jinrishici remain
deferred. No deployment/site push. See the coordination P4-B report for evidence/limits.

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
