// Render all SVG sources in figures/svg/ to 2400px-wide PNGs.
// Usage: NODE_PATH=<node workspace> node figures/render.js
const fs = require('fs');
const path = require('path');
const { Resvg } = require('@resvg/resvg-js');

const svgDir = path.join(__dirname, 'svg');
const outDir = __dirname;
const FONTS = [
  '/System/Library/Fonts/Supplemental/Arial.ttf',
  '/System/Library/Fonts/PingFang.ttc',
];

for (const f of fs.readdirSync(svgDir).filter((f) => f.endsWith('.svg'))) {
  const svg = fs.readFileSync(path.join(svgDir, f), 'utf8');
  const resvg = new Resvg(svg, {
    fitTo: { mode: 'width', value: 2400 },
    font: { fontFiles: FONTS, defaultFontFamily: 'Arial' },
  });
  const png = resvg.render().asPng();
  const out = path.join(outDir, f.replace(/\.svg$/, '.png'));
  fs.writeFileSync(out, png);
  console.log('rendered:', path.basename(out), (png.length / 1024).toFixed(0) + ' KB');
}
