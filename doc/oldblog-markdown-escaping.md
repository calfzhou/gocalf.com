# Old-blog Markdown escaping cleanup

Eureka audited all 74 Markdown files under `content/oldblog` on
`feature/oldblog-refine`. This is an authoring cleanup, not a rewrite of the
articles, algorithms, examples, dates or theme.

## Outcome

- Updated **67 articles**.
- Removed **1,658 escaping backslashes**.
- Added **136 inline-code spans across 17 articles**, including one in a summary.
- Preserved all other source characters, including line breaks and existing
  punctuation. New characters consist only of inline-code backticks.

## Plain text versus inline code

A hyphen inside a word and a dot in a version or filename do not ordinarily need
Markdown escaping. The old source escaped many punctuation marks indiscriminately;
that is consistent with conservative converter output, but the exact origin was
not established in this pass.

| Original source | Refined source | Reason |
| --- | --- | --- |
| `Self\-Descriptive Sentence` | `Self-Descriptive Sentence` | Ordinary prose, not code. |
| `10\.6\.8` | `10.6.8` | Ordinary version text. |
| `Ctrl\+O` | `Ctrl+O` | A shortcut label does not need the plus escaped. |
| `NVinject\.kext` | `` `NVinject.kext` `` | A literal filename benefits from code formatting. |
| `partial\_sort` | `` `partial_sort` `` | An actual API identifier. |
| `\$PATH` | `` `$PATH` `` | A literal environment variable, not math. |
| `3\.0\.\*` | `` `3.0.*` `` | A literal version pattern, not Markdown emphasis. |

Other inline-code conversions include driver filenames, Windows/registry paths,
function and variable names, boot options, the `<object>` tag, and URL rewrite
patterns. Backslashes inside code are literal, so Windows paths no longer need
doubled backslashes. Existing code spans and fenced blocks were not reformatted.

Link labels were cleaned without changing their destinations. Where a label is a
literal filename, code formatting stays inside the link. Existing Chinese corner
quotes around identifiers were retained rather than changing the prose again.

The embedded `rich-table` YAML in `python-read-write-excel` was handled separately:
only redundant escapes in its Markdown cell strings were removed; its structure,
quoting and rendered table were preserved.

## Escapes deliberately retained

Not every remaining backslash is redundant under the current Sidera configuration:

- **Math and executable/literal code:** TeX commands, delimiters, code samples,
  shortcode code bodies and URL destinations remain unchanged.
- **Block syntax:** escaped operators or numbered markers at the start of a line
  can prevent unintended lists or blockquotes. Existing line wrapping is preserved.
- **Blank placeholders:** the `\_\_` sequences in `self-descriptive-sentence`
  remain literal blanks rather than potential emphasis delimiters.
- **Smart typography:** unescaping apostrophes/quotes, repeated periods, double
  hyphens or `<<` can change their rendered characters. For example, the current
  renderer changes unescaped `<<` into `«`. Preserve such opt-out escapes when
  the literal character sequence matters, not simply to retain legacy typography.
  In a follow-up refinement, the twelve escaped trailing dots in the Chinese
  blockquote in `self-descriptive-sentence` were normalized to `……`; prose
  ellipses do not need literal-dot preservation or code formatting.
- **Automatic links:** ordinary non-link `www.…` references retain an escaped
  first dot to avoid silently adding hyperlinks. URL rewrite examples instead use
  code spans, which need no such escapes.
- **Literal dollar signs:** the Excel discussion retains `\$` where it means the
  dollar character, not a math delimiter.

One possible legacy typo was noticed but not changed: the second item in
`2011/puzzle-wwwdot-google-dotcom/index.md` ends with an escaped literal backtick
(`` D\` ``). Removing that character would be a content correction, not unescaping.

## Verification

- Hugo **0.166.0 extended** production build passed with minification and
  `--panicOnWarning`, using an isolated destination and cache under ignored `var/`.
- Compared rendered article-body HTML for **all 67 changed articles** against the
  previous committed version's build. Text, links, heading IDs, lists, tables,
  images and math are equivalent after accounting for the intentional inline-code
  wrappers and removal of visible escape backslashes from heading accessibility
  labels/tooltips. No unintended emphasis, autolinks or typographic substitutions
  remain in the comparison.
- Verified source changes consist only of removing backslashes and adding code
  backticks. Existing protected code/math/URL spans remain intact; front matter
  changes are restricted to summaries.
- `git diff --check` passed. Attachments, theme code, publication dates and slugs
  were not changed. No browser visual/interaction test was run.
