Static chart

Data: variable-width-column-chart.json
Render with Python 3.11+ (standard library only):
  python3 render.py variable-width-column-chart.json variable-width-column-chart.svg

All original data values, series order and labels are retained. Straight line segments, markers and linear axes are used. The variable-width chart retains the original mean-width times 0.2 gap formula and width/height labels. Original source is in original-source.zip for inspection only. No Highcharts or jQuery is executed or required.

This is a static reconstruction, not a pixel-identical capture. The old renderer/CDN version and inherited defaults were unpinned; this recipe explicitly sets palette, axes, typography, white background and legend layout. Charts with explicit original colors retain them. No hover, animation or series toggle is provided. No data is regenerated or resampled.
