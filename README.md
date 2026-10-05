# GoCalf

## Build and preview

Requires **Hugo 0.166.0 extended** and Git. Node, pnpm and Python are not needed to
build the site. Initialize the exact theme dependency after checkout:

```sh
git submodule update --init --recursive
make build
```

`make build` writes production output to `public/` and excludes drafts, future and
expired content. It does not clear old output; use a fresh destination for an
artifact intended for hosting:

```sh
mkdir -p var
run=$(mktemp -d "$PWD/var/hugo-build-XXXXXX")
hugo --environment production --destination "$run/public" --cacheDir "$run/cache" \
  --noBuildLock --panicOnWarning
```

Choose a free port and stop the server with Ctrl-C:

```sh
make serve port=14740    # published content
make preview port=14740  # also drafts and future content
```

`make server` is an alias for `make serve`. No install, clean, push or deployment
target is provided. Existing output, backups and user caches are never deleted by
these recipes. For authoritative comparisons, build into a fresh directory.

## Create content

```sh
make note slug=new-note title='A new note'
make post slug=new-post title='A new blog post'
make coding slug=new-problem title='A new coding problem'
make page slug=new-page title='A standalone page'
make draft slug=new-draft title='A standalone draft'
```

Slugs use lowercase ASCII letters, digits and internal hyphens, not paths. Titles
are separate Unicode strings; quote them for your shell. They are passed as data,
not shell code, and JSON-escaped into YAML strings. Existing bundles are never
overwritten. All kinds start with `draft: true`; review the content, then explicitly
set it to `false` to publish. New dates are set at creation; build/commit does not
change existing article dates. Blog bundles live under `content/blog/YYYY/` and
use the publication date in their public URL. Notes/Coding use their collections;
page/draft create standalone root bundles.

For other native paths, use Hugo directly (do not use `--force`):

```sh
hugo new content --kind note notes/another-note
hugo new content standalone.md
```

Hugo's direct CLI derives a title from the destination name. Optionally provide
`HUGO_NEW_TITLE='An exact title'` in its environment. Native CLI paths are more
permissive than the Make wrappers; choose a destination inside `content/`.

### Markdown and resources

Use **YAML `---` front matter**. Native fields include `title`, `date`, `lastmod`,
`draft`, `type`, `tags` and `categories`; custom Sidera fields belong under `params`.
Collections own their presets—ordinary articles do not repeat `preset` or notebook
identities. Blog archetypes use `type: story`.

Keep images, diagrams and public source files next to `index.md`. Ordinary relative
Markdown links such as `../other-note/index.md` work in the editor and resolve to
public URLs. Use `![Description](image.png)`; put optional image attributes on the
following line. Use native headings, not manually assigned compatibility IDs.

The Coding bundle includes unchanged example `solution.py` / `solution_test.py`
companions and `{{< snippet src="solution.py" >}}` inclusions. They are public code
resources; creation and building never execute them. The test example uses pytest
only if you separately choose to run it. Replace its demonstration before publishing.
Coding example Input/Output/Explanation rows use a single trailing backslash when
line separation is intentional. Preserve real math; escape literal currency dollars.

## Obsidian vault

Open `content/` as the vault. Its `.obsidian/`, `_templates/`, `.gitignore` and
`.editorconfig` belong to the editor. Keep Markdown-relative links and adjacent
attachments. Templater maps Notes, Coding and Blog to the matching templates.
Both the Hugo Coding archetype and the editor Coding template provide Python companion
files. The editor copies template text only and leaves existing companions untouched.

Hugo's content mount and ignore rules exclude editor settings/plugins/templates,
local trash/caches, `_utils`, Python bytecode, edit-history files and the consistency
report from all output formats. These exclusions are not Git secrecy: tracked plugin
settings are still part of repository history. Never put credentials in tracked files
or public bundle resources. Do not mount the whole vault as `static` or shared snippets.

Linter retains its existing lint-on-save behavior; automatic YAML timestamps are off.
No editor plugin is installed or executed by Make/Hugo. Edit `date`/`lastmod`
intentionally; filesystem modification time is not a publication timestamp.

## Hosting

The configured canonical URL is `https://gocalf.com/`. Serve the generated directory
at the domain root, preserve trailing-slash routes, and serve `404.html` with HTTP
404 for missing URLs. The static `CNAME` contains the custom domain. Validate HTTPS,
assets and existing URLs on the chosen host. A build does not configure DNS or Pages.
Comments and source-edit links are optional and currently off; configure only this
site's actual Giscus/source identity before enabling them.
