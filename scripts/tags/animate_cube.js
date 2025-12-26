'use strict';

module.exports = ctx => function (args) {
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
  ];
  args = ctx.args.map(args, ['size', 'width', 'height', ...cubeParamKeys]);
  const { size = '3', width = '300px', height = '319px', others, ...cubeParams } = args;
  const control = Object.keys(cubeParams).map(key => `${key}=${cubeParams[key]}`).join('&');
  const id = 'animcube-div-' + Math.random().toString(36).substring(2);
  return `<div id="${id}" style="width: ${width}; height: ${height}"><script>window.addEventListener('load', function(){ AnimCube${size}("id=${id}&${control}") })</script></div>`;
  // return `<div style="width: ${width}; height: ${height}"><script>AnimCube${size}("${control}")</script></div>`;
};
