'use strict'

function inlineImg(alt, src) {
  return `<img alt="${alt}" src="${src}" style="border-radius: 0; display: inline-block;">`
}

hexo.extend.tag.register('badge_github', function (args) {
  args = hexo.args.map(args, ['release'], ['user', 'repo'])
  const { user, repo, release } = args
  const parts = []
  const repoImg = inlineImg(
    `${user}/${repo}`,
    `https://img.shields.io/static/v1?label=${user}&message=${repo}&color=blue&logo=github`
  )
  parts.push(`<a href="https://github.com/${user}/${repo}">${repoImg}</a>`)
  parts.push(inlineImg('stars', `https://img.shields.io/github/stars/${user}/${repo}?logo=.&style=social`))
  parts.push(inlineImg('forks', `https://img.shields.io/github/forks/${user}/${repo}?logo=.&style=social`))
  parts.push(inlineImg('updated', `https://img.shields.io/github/last-commit/${user}/${repo}?label=`))
  if (release) {
    parts.push(inlineImg('release', `https://img.shields.io/github/v/release/${user}/${repo}?label=`))
    parts.push(inlineImg('release date', `https://img.shields.io/github/release-date/${user}/${repo}?label=`))
  }
  return '<p>' + parts.join(' ') + '</p>'
})

hexo.extend.tag.register('animcube', function (args) {
  const cubeParamKeys = [
    'align',
    'bgcolor',
    'borderwidth',
    'butbgcolor',
    'buttonbar',
    'buttonheight',
    'clickprogress',
    'colors',
    'colorscheme',
    'config',
    'counter',
    'cubecolor',
    'demo',
    'doublespeed',
    'edit',
    'facelets',
    'fonttype',
    'gabbacolors',
    'hint',
    'hintborder',
    'hinthoriz',
    'hintvert',
    'initmove',
    'initrevmove',
    'metric',
    'move',
    'movetext',
    'movetextspace',
    'perspective',
    'pos',
    'position',
    'randmoves',
    'repeat',
    'scale',
    'scramble',
    'scw',
    'sign',
    'slidercolor',
    'snap',
    'speed',
    'supercube',
    'superfacelets',
    'textsize',
    'troughcolor',
    'wca',
    'yz',
    // My extra parameters.
    'markers',
  ]
  args = hexo.args.map(args, ['size', 'width', 'height', ...cubeParamKeys])
  const { size = '3', width = '300px', height = '319px', others, ...cubeParams } = args
  const control = Object.keys(cubeParams).map(key => `${key}=${cubeParams[key]}`).join('&')
  const id = 'animcube-div-' + Math.random().toString(36).substring(2)
  return `<div id="${id}" style="width: ${width}; height: ${height}"><script>window.addEventListener('load', function(){ AnimCube${size}("id=${id}&${control}") })</script></div>`
  // return `<div style="width: ${width}; height: ${height}"><script>AnimCube${size}("${control}")</script></div>`
})

hexo.extend.tag.register('invert', function (args, content) {
  args = hexo.args.map(args, ['when'])
  const { when = 'dark' } = args
  const inner = hexo.render.renderSync({ text: content, engine: 'markdown' }) //.split('\n').join('')
  const classes = []
  if (when === 'dark' || when === 'always') {
    classes.push('invert-when-dark')
  }
  if (when === 'light' || when === 'always') {
    classes.push('invert-when-light')
  }
  return `<div class="${classes.join(' ')}">${inner}</div>`
}, true)

hexo.extend.tag.register('asset_code', require('./asset_code')(hexo), { async: true })
