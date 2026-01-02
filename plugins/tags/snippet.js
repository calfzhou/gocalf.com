'use strict';

/**
 * Tag to import code snippets in markdown.
 *
 * {% snippet path/to/file [title] [lang:language] [from:line] [to:line] %}
 *
 * Note: the `path/to/file` can either relative to the current file or the `source` directory.
 */

const lib_path = require('path');
const hexo_util = require("hexo-util");
const fs = require('fs');

module.exports = hexo => function (args) {
  args = hexo.args.map(args, ['lang', 'from', 'to'], ['path', 'title']);
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

  const Asset = hexo.model('Asset');
  let doc = Asset.findOne({ path: lib_path.join(lib_path.dirname(source), path) });
  if (!doc) {
    doc = Asset.findOne({ path });
  }
  if (!doc) {
    hexo.log.warn(`[tags/snippet] Asset not found: ${path} (relative to ${source}, or absolute)`);
    return;
  }

  const buffer = fs.readFileSync(doc.source);
  let code = buffer.toString();
  const lines = code.split('\n');
  code = lines.slice(from, to).join('\n').trim();

  const caption = `<span><a href="${hexo_util.url_for.call(hexo, doc.path)}">${title}</a></span>`;
  if (hexo.extend.highlight.query(hexo.config.syntax_highlighter)) {
    const options = {
        lang,
        caption,
        lines_length: lines.length
    };
    return hexo.extend.highlight.exec(hexo.config.syntax_highlighter, {
        context: hexo,
        args: [code, options]
    });
  }

  return `<pre><code>${code}</code></pre>`;
}
