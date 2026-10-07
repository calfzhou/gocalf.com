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

## Theme manual

The theme-owned Sidera manual is mounted at `/sidera/`, with the **Sidera** menu
entry immediately before **关于**. Its source stays in `themes/sidera/docs/content`;
do not copy it into the site content tree. Updating the pinned theme also updates
the bundled manual. It uses Chinese theme controls around the English manual body,
the default docs sidebar, explicit dates and AI disclosure. Manual comments remain
disabled independently of the site's article comment setting.

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

## Authors

The native site cascade defaults content to `authors: [calf]`. For a post written
from an AI participant's own perspective, use top-level `authors: [gocalf-ai]`.
The shared display identity is **GoCalf AI**; identify the actual participant, such
as Eureka, in the post itself. This does not imply review or endorsement by Calf.
AI assistance on a Calf-authored post does not automatically change its author.

Profiles live in `content/authors/`. Explicit `authors: []` opts out of the default;
the mounted Sidera manual uses no authors and retains its separate MIT notice.
The article license uses `{page.authors}` for native linked author names. Keep the
AI participation label (`params.ai_label`) independent of the author assignment.

## Obsidian vault

Open `content/` as the vault. Its `.obsidian/`, `_templates/`, `.gitignore` and
`.editorconfig` belong to the editor. Keep Markdown-relative links and adjacent
attachments. Templater maps Notes, Coding and Blog to the matching templates.
Both the Hugo Coding archetype and the editor Coding template provide Python companion
files. The editor copies template text only and leaves existing companions untouched.

### Create a note with Templater

Create an **empty** note in `notes/`, `coding/` or `blog/`, or use Templater's
“Create new note from template” command with the matching template. Vault paths
are relative to `content/`, so do not prefix them with `content/` or `source/`.

- An `Untitled` / `未命名` note asks for an ASCII slug and then a display title.
- A named note such as `notes/my-note.md` uses `my-note` as its slug, asks for its
  display title, and becomes `notes/my-note/index.md`. A Unicode/spaced filename
  asks for a separate slug while preserving that name as the suggested title.
- New blog bundles use `blog/YYYY/slug/index.md`, with YYYY taken from the note's
  creation date. Coding bundles use `coding/slug/index.md`.
- An empty `index.md` already placed in `notes/slug/`, `coding/slug/` or
  `blog/YYYY/slug/` is completed in place; its title is suggested from the bundle
  name, not the word “index”. Section `_index.md` and collection-root `index.md`
  are not article-template targets. Nor is an extra Markdown resource in an existing
  leaf bundle a new article.
- Every generated article uses YAML, `draft: true`, one captured creation timestamp
  for both `date` and `lastmod`, and the current native fields/shortcodes. Review it
  and set `draft: false` when ready. Existing content or front matter is rejected,
  rather than replacing it or resetting authored dates.
- Cancelling or entering an invalid slug/title does not move the note or create
  companions. An existing destination bundle is never overwritten. Coding loads its
  companion template text before moving the note, preserves existing companion files
  in an in-place bundle, and never runs Python.

These templates are for new empty articles, not mass conversion or template insertion
into an existing article. Obsidian and Templater still control their normal dialog,
file-event and YAML serialization behavior; the site does not install or run them.

Hugo's native ignore rules exclude editor settings/plugins/templates,
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
Comments use this site's verified Giscus repository and Announcements category.
Source-edit links remain off.

The Pages workflow builds on pushes and pull requests to `main`, using the exact
committed theme submodule and checksum-verified Hugo **0.166.0 extended**. It uploads
a build artifact and **automatically deploys successful pushes to `main`** to GitHub
Pages. Pull requests build and upload an artifact but never deploy. Failed, cancelled
or skipped builds cannot publish. No recurring build or deployment approval is required
for successful main pushes under the current Pages environment configuration.

Manual workflow runs remain available: on `main`, enable `deploy` to publish, or leave
it disabled for a build-only run. Other branches cannot deploy. Pages still requires
the repository's environment/permissions to be configured. No Node/pnpm installation
is involved.

The workflow's Linux binary URL and SHA-256 are pinned together; update and verify
both when deliberately upgrading Hugo. Local builds do not run this installer.


## Visitor services

`params.comments = true` enables eligible article comments through the configured
GoCalf Giscus repository/category. Identity follows each native article pathname;
`strict = false` retains the existing matching policy. Queries and heading fragments
do not change the discussion term. Do not submit test comments or reactions from a
local preview: the provider uses real discussions.

`params.jinrishici = true` shows the welcome sentence before the first left-side menu,
without replacing Sidera's collection/sidebar defaults. A small site-owned menu
component override preserves the theme's native menu lookup and adds the welcome
partial only once. Set the flag to false to omit the widget and its loader.

The browser loads the official Jinrishici SDK; returned sentence text is assigned
with `textContent`, not parsed as HTML. One empty line is reserved until a valid
sentence arrives, including when JavaScript is unavailable, the service fails, or
the request takes too long. There is no placeholder text. The existing 15px widget
font is unchanged; narrower side padding lets typical 12/16-character sentences
fit one line. Longer sentences can still wrap without clipping. The SDK
is trusted third-party JavaScript running in the page; it contacts its provider and
may keep its own browser identifier. Nothing is fetched during the Hugo build, and
no provider token is embedded in source or logs.

These integrations use trusted native templates/scripts. Keep Markdown raw-HTML
rendering disabled; article authors do not need permission to inject scripts.
