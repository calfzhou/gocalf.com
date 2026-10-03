# GoCalf

## Hugo migration (local branch; P4-C review)

This branch now contains **414 live articles**: 16 accepted B pilots and 398 C
conversions. The retired Stellar wrapper and 75 editor/data/template/style files
remain preserved under `source/`, outside Hugo publication. Coding `_utils` retains
its import geometry but is explicitly excluded from output.

Use Hugo **0.166.0 extended** directly. Do not install/prepare packages for this
preview; the legacy Makefile/package scripts below still run Hexo.

```sh
# Choose a free port; stop your preview with Ctrl-C.
hugo server --bind 127.0.0.1 --port 14740 --disableFastRender

# Fresh static validation; do not interfere with an existing preview lock.
run=$(mktemp -d "$PWD/var/hugo-build-XXXXXX")
hugo --destination "$run/public" --cacheDir "$run/cache" --noBuildLock --panicOnWarning
```

Never target the preserved sibling `gocalf.com-public-hexo` as output. All migrated
Markdown uses **YAML `---` front matter** and preserved authored instants. Ordinary
headings use native Hugo IDs; explicit IDs require a specific reviewed need. Coding
example fields use explicit backslash hard breaks, not global hard-wrapping. Image
attributes follow native standalone/quoted-block placement.

The existing Sidera pin **1e5c26d** is unchanged by C. Fresh strict normal/all-states
builds, native metadata/source/resource checks, retained B regression and bounded
expanded browser checks pass. See coordination `P4-C.md` and `p4-c/` for batch history,
complete source accounting and limits. **C awaits user review**, not production
certification. Comments remain off; Jinrishici/edit links remain deferred. No site
push/deploy, anonymous candidate reproduction or P4-D/E execution is implied.

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
