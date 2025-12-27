'use strict';

// Reference:
// https://github.com/tcatche/hexo-filter-link-post

const lib_path = require('path');
const { relative_url } = require('hexo-util');

const permalinks = new Map(); // post source -> post permalink

module.exports.preProcess = data => {
  permalinks.set(data.source, data.permalink);
};

module.exports.convertLinks = function(data) {
  // Regex matching markdown links '[name](link)'.
  const mdLinkRe = /\[([^\]]+)\]\(([^)]+)\)/g;
  const replacements = [];

  let match;
  while ((match = mdLinkRe.exec(data.content)) !== null) {
    const [fullMatch, name, link] = match;

    // Check if the link ends with '.md' or contains '.md#', and does not contains '://'.
    if (/\.md(#|$)/.test(link) && !/:\//.test(link)) {
      const [relativePath, anchor = ''] = link.split('#');

      const currDir = lib_path.dirname(data.source);
      const targetPath = lib_path.normalize(lib_path.join(currDir, relativePath));

      const targetPermalink = permalinks.get(targetPath);
      if (!targetPermalink) {
        console.warn(`md_path_to_permalink: ${data.source}: found orphans link "${fullMatch}"`);
        continue; // Skip if no permalink found
      }

      const newLink = `${relative_url(data.permalink, targetPermalink)}${anchor ? `#${anchor}` : ''}`;
      const replacement = `[${name}](${newLink})`;
      replacements.push({
        start: match.index,
        end: match.index + fullMatch.length,
        replacement,
      });
    }
  }

  // Apply replacements in reverse order to avoid index shifting.
  let content = data.content;
  replacements.reverse().forEach(({ start, end, replacement }) => {
    content = content.slice(0, start) + replacement + content.slice(end);
  })

  data.content = content;
  return data;
}
