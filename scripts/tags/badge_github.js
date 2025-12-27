'use strict';

function inlineImg(alt, src) {
  return `<img alt="${alt}" src="${src}" style="border-radius: 0; display: inline-block;">`;
}

module.exports = ctx => function (args) {
  args = ctx.args.map(args, ['release', 'branch'], ['user', 'repo']);
  const { user, repo, release, branch } = args;
  const parts = [];
  const repoImg = inlineImg(
    `${user}/${repo}${branch ? ` (${branch})` : ''}`,
    `https://img.shields.io/static/v1?label=${user}&message=${repo}${branch? ` (${branch})` : ''}&color=blue&logo=github`
  );
  parts.push(`<a href="https://github.com/${user}/${repo}">${repoImg}</a>`);
  parts.push(inlineImg('stars', `https://img.shields.io/github/stars/${user}/${repo}?logo=.&style=social`));
  parts.push(inlineImg('forks', `https://img.shields.io/github/forks/${user}/${repo}?logo=.&style=social`));
  parts.push(inlineImg('updated', `https://img.shields.io/github/last-commit/${user}/${repo}${branch ? `/${branch}` : ''}?label=`));
  if (release) {
    parts.push(inlineImg('release', `https://img.shields.io/github/v/release/${user}/${repo}?label=`));
    parts.push(inlineImg('release date', `https://img.shields.io/github/release-date/${user}/${repo}?label=`));
  }
  return '<p>' + parts.join(' ') + '</p>';
};
