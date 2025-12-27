'use strict';

const { escapeHTML, relative_url } = require('hexo-util');

const posts = new Map(); // post permalink -> post data
const linkRe = /(?<!\!)\[[^\]]+\]\(([^)]+)\)|<([^>]+)>/g;

module.exports.preProcess = data => {
  data._mentions = new Set();
  data._backlinks = new Set();
  posts.set(data.permalink, data);
  return data;
};

module.exports.processSite = data => {
  for (const match of data.content.matchAll(linkRe)) {
    let link = match[1] || match[2];
    const url = new URL(link, data.permalink);
    url.hash = '';
    url.search = '';
    link = url.href;
    if (link != data.permalink && posts.has(link)) {
      data._mentions?.add(link);
      posts.get(link)._backlinks?.add(data.permalink);
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
  data.references.push(...hackReferences(Array.from(data._mentions), '本文引用', data.permalink));
  data.references.push(...hackReferences(Array.from(data._backlinks), '反向引用', data.permalink));
  return data;
};
