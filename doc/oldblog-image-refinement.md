# Old-blog image shortcode refinement

Eureka audited every `image` shortcode in `content/oldblog` on
`feature/oldblog-refine`. This pass changes image authoring only; prose, dates,
front matter, attachments and the Sidera theme are unchanged.

## Outcome

- Audited **268 shortcodes in 32 articles**.
- Converted **78 images in 30 articles** to Markdown, using the existing caption
  as the image description instead of the migration-generated filename alt.
- Retained **190 shortcodes in 12 articles**, unchanged, because they enable the
  original-image viewer. Two of these articles have no convertible images.
- All referenced source and original image files exist locally.

## Exceptions and unusual cases

### Original-image viewer: retained

Sidera's `original` parameter is not just a duplicate URL. It adds a clickable
image and progressive zoom/pan/download viewer. Ordinary Markdown images do not
receive that viewer; replacing these shortcodes would remove functionality.

- **180 screenshots** in `2011/zelda-tp-ch1` through `zelda-tp-ch9` and
  `2012/zelda-tp-epilogue` use `original=src` and `width=500`. These still provide
  expansion beyond the 500px presentation. Retained even though the two URLs match.
- **9 thumbnail/original pairs** in `2012/zelda-tp-appendix` use
  `heart_pieces_1_small.jpg` through `heart_pieces_9_small.jpg`, each opening its
  corresponding `heart_pieces_N.jpg`. All are inside the numbered walkthrough.
- **1 thumbnail/original pair** in `2011/ipad2-433-jailbreak` uses
  `cydia-ipad2-ios433-225x300.jpg`, opening `cydia-ipad2-ios433.jpg`. It also has an
  explicit caption inside a list; Sidera suppresses automatic Markdown captions
  there, so a plain Markdown replacement would lose both the viewer and caption.

All parameters, including alt text and explicit empty captions, remain unchanged
on these retained shortcodes. Dropping their viewer is a separate editorial choice,
not a syntax-equivalent conversion.

### Width without a viewer: converted

Prefer Sidera's `![caption|width](src)` syntax over separate next-line width
attributes. Both SVG widths are preserved, and the suffix is excluded from the
rendered caption and alt text:

- `2011/about-paper-size`: `![889x1194 24 开本|346](paper_24k.svg)`.
- `2011/clock-hands-relative-motion`: `![4:21:49.09，时针与分针重合|284](4h21m49s.svg)`.

### Literal angle brackets: converted and rendering checked

`2011/bluehost-mailbox`, `godaddy_dns.png`: the caption includes
`mail.<yourdomain>.com`. Markdown uses `mail.&lt;yourdomain&gt;.com` to keep those
brackets literal. Backslash escaping was tested but exposed backslashes through
Sidera's plain-text image hook; entity encoding preserves the exact rendered
caption and alt text without modifying the theme.

### Empty captions

- `2014/make-mac-better-for-development`, `iterm2_logo.png`: converted to
  `![](iterm2_logo.png)`. This keeps the logo caption-free and removes its filename
  alt; no new description was invented. The surrounding prose names iTerm2.
- **17 retained viewer images** have explicit empty captions: `tp_ch04_19`,
  `tp_ch04_20`, `tp_ch04_21`, `tp_ch04_23`, `tp_ch05_11`, `tp_ch06_13`,
  `tp_ch07_15`, `tp_ch07_26`, and the nine `heart_pieces_N_small` thumbnails.
  Their original caption suppression and alt text remain intact.

## Complete article inventory

Paths below are relative to `content/oldblog`; counts describe this refinement pass.

| Article | Converted | Retained for viewer |
| --- | ---: | ---: |
| [2011/5x5-sudoku-in-vcube7](../content/oldblog/2011/5x5-sudoku-in-vcube7/index.md) | 3 | 0 |
| [2011/about-paper-size](../content/oldblog/2011/about-paper-size/index.md) | 1 | 0 |
| [2011/bluehost-mailbox](../content/oldblog/2011/bluehost-mailbox/index.md) | 1 | 0 |
| [2011/check-udisk](../content/oldblog/2011/check-udisk/index.md) | 4 | 0 |
| [2011/clock-hands-relative-motion](../content/oldblog/2011/clock-hands-relative-motion/index.md) | 2 | 0 |
| [2011/dell-e6400-install-mac](../content/oldblog/2011/dell-e6400-install-mac/index.md) | 3 | 0 |
| [2011/dell-e6400-mac-10-6-8](../content/oldblog/2011/dell-e6400-mac-10-6-8/index.md) | 1 | 0 |
| [2011/google-doodle-calder](../content/oldblog/2011/google-doodle-calder/index.md) | 1 | 0 |
| [2011/hide-drive-q](../content/oldblog/2011/hide-drive-q/index.md) | 4 | 0 |
| [2011/ipad2-433-jailbreak](../content/oldblog/2011/ipad2-433-jailbreak/index.md) | 0 | 1 |
| [2011/iphone-dev-hide-status-bar](../content/oldblog/2011/iphone-dev-hide-status-bar/index.md) | 1 | 0 |
| [2011/iphone-dev-progressview-in-alertview](../content/oldblog/2011/iphone-dev-progressview-in-alertview/index.md) | 1 | 0 |
| [2011/manufactoria](../content/oldblog/2011/manufactoria/index.md) | 1 | 0 |
| [2011/win7-god-mode](../content/oldblog/2011/win7-god-mode/index.md) | 3 | 0 |
| [2011/zelda-tp-ch1](../content/oldblog/2011/zelda-tp-ch1/index.md) | 1 | 18 |
| [2011/zelda-tp-ch2](../content/oldblog/2011/zelda-tp-ch2/index.md) | 1 | 12 |
| [2011/zelda-tp-ch3](../content/oldblog/2011/zelda-tp-ch3/index.md) | 1 | 11 |
| [2011/zelda-tp-ch4](../content/oldblog/2011/zelda-tp-ch4/index.md) | 2 | 22 |
| [2011/zelda-tp-ch5](../content/oldblog/2011/zelda-tp-ch5/index.md) | 1 | 19 |
| [2011/zelda-tp-ch6](../content/oldblog/2011/zelda-tp-ch6/index.md) | 2 | 14 |
| [2011/zelda-tp-ch7](../content/oldblog/2011/zelda-tp-ch7/index.md) | 3 | 27 |
| [2011/zelda-tp-ch8](../content/oldblog/2011/zelda-tp-ch8/index.md) | 2 | 16 |
| [2011/zelda-tp-ch9](../content/oldblog/2011/zelda-tp-ch9/index.md) | 3 | 32 |
| [2011/zelda-tp-characters](../content/oldblog/2011/zelda-tp-characters/index.md) | 11 | 0 |
| [2011/zelda-tp-intro](../content/oldblog/2011/zelda-tp-intro/index.md) | 2 | 0 |
| [2012/chromatron](../content/oldblog/2012/chromatron/index.md) | 2 | 0 |
| [2012/iphone-dev-range-slider](../content/oldblog/2012/iphone-dev-range-slider/index.md) | 1 | 0 |
| [2012/iphone-dev-resizable-image](../content/oldblog/2012/iphone-dev-resizable-image/index.md) | 1 | 0 |
| [2012/zelda-tp-appendix](../content/oldblog/2012/zelda-tp-appendix/index.md) | 3 | 9 |
| [2012/zelda-tp-epilogue](../content/oldblog/2012/zelda-tp-epilogue/index.md) | 0 | 9 |
| [2013/excel-variable-width-column-chart](../content/oldblog/2013/excel-variable-width-column-chart/index.md) | 12 | 0 |
| [2014/make-mac-better-for-development](../content/oldblog/2014/make-mac-better-for-development/index.md) | 4 | 0 |

## Verification

- Built production output into fresh, isolated destinations before and after the
  edits, with Hugo **0.166.0 extended**, minification and `--panicOnWarning`.
  Both builds passed with identical page/resource counts.
- Compared rendered HTML for all **268 audited images**: all 78 conversions retain
  their exact captions, resolved image URLs and explicit widths, with caption text
  now used as alt; all 190 retained images have identical parsed image attributes,
  figure/caption data and original-viewer links.
- Verified published image/original bytes are unchanged and article image counts
  are unchanged. No referenced images were lost.
- Verified that source outside the converted image expressions, including front
  matter and all retained shortcodes, is unchanged; `git diff --check` passed.
- No browser visual or interaction test was run. The viewer implementation was not
  changed; its generated links and markup were checked rather than re-tested live.
