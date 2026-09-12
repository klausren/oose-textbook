// Render only the ch09 SVGs to PNG, reusing the book's render settings.
const fs = require('fs');
const path = require('path');
const { Resvg } = require('@resvg/resvg-js');
const svgDir = path.join(__dirname, '..', 'svg');
const outDir = path.join(__dirname, '..');
const FONTS = ['/System/Library/Fonts/Supplemental/Arial.ttf',
               '/System/Library/Fonts/PingFang.ttc'];
const want = process.argv.slice(2);
for (const f of fs.readdirSync(svgDir).filter((f) => f.endsWith('.svg'))) {
  if (want.length && !want.some((w) => f.includes(w))) continue;
  const svg = fs.readFileSync(path.join(svgDir, f), 'utf8');
  const resvg = new Resvg(svg, {
    fitTo: { mode: 'width', value: 2400 },
    font: { fontFiles: FONTS, defaultFontFamily: 'Arial' },
  });
  const png = resvg.render().asPng();
  fs.writeFileSync(path.join(outDir, f.replace(/\.svg$/, '.png')), png);
  console.log('rendered:', f.replace(/\.svg$/, '.png'));
}
