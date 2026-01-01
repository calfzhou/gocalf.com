'use strict';

const { escapeHTML, relative_url } = require('hexo-util');

const LINK_RE = /(?<!\!)\[[^\]]+\]\(([^)]+)\)|<([^>]+)>/g;
const posts = new Map(); // post permalink -> post data { title, mentions, backlinks }

module.exports.preProcess = data => {
  if (posts.has(data.permalink)) {
    posts.get(data.permalink).title = data.title;
  } else {
    posts.set(data.permalink, {
      title: data.title,
      mentions: new Set(),
      backlinks: new Set(),
    });
  }

  return data;
};

module.exports.processSite = data => {
  const { mentions } = posts.get(data.permalink);
  if (mentions.size > 0) {
    // This only happens when file is modified during `hexo server`.
    // Need to clear previous mentions' backlinks.
    mentions.forEach(link => posts.get(link)?.backlinks?.delete(data.permalink));
    mentions.clear();
  }

  for (const match of data.content.matchAll(LINK_RE)) {
    let link = match[1] || match[2];
    const url = new URL(link, data.permalink);
    url.hash = '';
    url.search = '';
    link = url.href;
    if (link != data.permalink && posts.has(link)) {
      mentions.add(link);
      posts.get(link).backlinks.add(data.permalink);
    }
  }
  return data;
};

const hackReferences = (links, title, permalink) => {
  // const items = links.map(link => `[${posts.get(link).title}](${relative_url(permalink, link)})`);
  const items = links.map(link => `<p><a href="${relative_url(permalink, link)}">${escapeHTML(posts.get(link).title)}</a></p>`);
  if (items.length > 0) {
    items[0] = `<p>${title}</p><ul><li class="post-title">${items[0]}`;
    items[items.length - 1] += '</li></ul>';
  }
  return items;
};

module.exports.postProcess = data => {
  // 暂时先放在 references 里，省的改主题。
  data.references ||= [];
  const { mentions, backlinks } = posts.get(data.permalink);
  data.references.push(...hackReferences(Array.from(mentions), '本文引用', data.permalink));
  data.references.push(...hackReferences(Array.from(backlinks), '反向引用', data.permalink));
  return data;
};
