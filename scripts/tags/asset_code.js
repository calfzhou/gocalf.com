'use strict';

/**
 * Asset code tag.
 *
 * {% asset_code path/to/file [title] [lang:language] [from:line] [to:line] %}
 *
 * Note: the `path/to/file` is relative to the `source` directory.
 */

const lib_path = require('path');
const hexo_util = require("hexo-util");
const fs = require('fs');

module.exports = ctx => function (args) {
  args = ctx.args.map(args, ['lang', 'from', 'to'], ['path', 'title']);
  let { lang = '', from = 0, to = -1, path, title = '' } = args;
  from = from > 0 ? from - 1 : 0;

  // Exit if path is not defined.
  if (!path) {
    return;
  }

  // If the language is not defined, use file extension instead.
  lang = lang || lib_path.extname(path).substring(1);

  // If the title is not defined, use file name instead.
  title = title || lib_path.basename(path);

  // Get the path of the source Markdown file relative to the Hexo source/ directory.
  const { source } = this;

  const Asset = ctx.model('Asset');
  let doc = Asset.findOne({ path: lib_path.join(lib_path.dirname(source), path) });
  if (!doc) {
    doc = Asset.findOne({ path });
  }
  if (!doc) {
    ctx.log.warn(`[tags/asset_code] Asset not found: ${path} (relative to ${source}, or absolute)`);
    return;
  }

  const buffer = fs.readFileSync(doc.source);
  let code = buffer.toString();
  const lines = code.split('\n');
  code = lines.slice(from, to).join('\n').trim();

  const caption = `<span><a href="${hexo_util.url_for.call(ctx, doc.path)}">${title}</a></span>`;
  if (ctx.extend.highlight.query(ctx.config.syntax_highlighter)) {
    const options = {
        lang,
        caption,
        lines_length: lines.length
    };
    return ctx.extend.highlight.exec(ctx.config.syntax_highlighter, {
        context: ctx,
        args: [code, options]
    });
  }

  return `<pre><code>${code}</code></pre>`;
}
