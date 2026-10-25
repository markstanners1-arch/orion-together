# Builds index.html for the "One sky, together" project site (together.oneoffx.co.uk).
# Words: body.html. Progress figures: progress.json ({{contributors}}, {{hours}}).
# Styles and the upload box were copied once from the Gosforth Skies site (_css.css, _form.html, _script.html);
# the upload box talks to the same upload Worker, which allows this site's address.
import json
from pathlib import Path

R = Path(__file__).parent
p = json.loads((R / 'progress.json').read_text(encoding='utf8'))
body = (R / 'body.html').read_text(encoding='utf8')
body = body.replace('{{form}}', (R / '_form.html').read_text(encoding='utf8'))
for k, v in p.items():
    body = body.replace('{{' + k + '}}', str(v))
page = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>One sky, together</title>
<meta name="description" content="A community astrophotography project: many telescopes, one picture, credited to everyone who took part.">
<link rel="stylesheet" href="fonts/fonts.css">
<style>{(R / '_css.css').read_text(encoding='utf8')}</style>
</head>
<body>
{body}
{(R / '_script.html').read_text(encoding='utf8')}
</body>
</html>
'''
(R / 'index.html').write_text(page, encoding='utf8')
print('wrote index.html', len(page))
