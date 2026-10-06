# Site-owned AnimCube integration

The six original minified libraries (sizes 2–7) remain byte-identical to the migration
baseline. Only the actually used sizes load on pages containing cube shortcodes.
No Sidera component/library or package install is required.

Original GoCalf library update **cb52740** identifies fork source
https://github.com/calfzhou/AnimCubeJS/commit/727ce2ea6336d2e202f25791c289ece367407bde .
That exact source was fetched read-only over anonymous HTTPS to verify provenance,
parameter parsing and the MIT notice. Required notice is retained at
`static/js/plugins/LICENSE-AnimCubeJS.txt` and publishes beside the preserved libraries.
The fork includes GoCalf's markers extension. The historical minifier command is not
recorded here; no claim that rebuilding latest upstream reproduces the original blobs.

Use native named string parameters, e.g. `animcube size="3" config="cube.conf"
move="R U R'"`; outer container `%`, nested leaf `<`, as with Sidera's other leaves.
Only audited data options are supported. Width accepts `100%` or positive pixels;
height is positive pixels. Config must be an existing adjacent `.conf` resource.
There is no visible configuration link/control; the resource remains public because
the animation needs it. Its basename stays in the library input because the original library resolves it
relative to the canonical page URL; the native resource is published unchanged.

The controller selects only known constructors, serializes inert JSON attributes,
and URL-encodes each value; no author-provided JS, raw HTML or dynamic function name.
Original libraries contain eval-based direct-access developer helpers, but shortcode
inputs do not expose those APIs or set `acjs_*` globals. Libraries are trusted site
assets, not a sandbox for untrusted executable code. Config requests remain same-origin.
No remote library fetch, iframe provider or source execution is introduced.

Cubes initialize when their enclosing native disclosures become visible, at most once;
local resize hooks preserve fold/grid layout. No-JS keeps explanatory prose/formulas
and an honest message; it is not interactive parity. UI retains upstream canvas input
behavior, not a newly certified keyboard/assistive-technology cube editor.
