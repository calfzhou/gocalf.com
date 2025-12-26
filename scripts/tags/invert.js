'use strict';

/**
 * Invert image color theme tag.
 *
 * {% invert [when:dark/light/always] %}
 * Content
 * {% endinvert %}
 *
 * when:
 *   - dark: invert image color when in dark mode
 *   - light: invert image color when in light mode
 *   - always: always invert image color
 *
 * Default is 'dark'.
 */

module.exports = ctx => function (args, content) {
  args = ctx.args.map(args, ['when']);
  const { when = 'dark' } = args;

  const inner = ctx.render.renderSync({ text: content, engine: 'markdown' }); //.split('\n').join('')
  const classes = [];
  if (when === 'dark' || when === 'always') {
    classes.push('invert-when-dark');
  }
  if (when === 'light' || when === 'always') {
    classes.push('invert-when-light');
  }
  return `<div class="${classes.join(' ')}">${inner}</div>`;
};
