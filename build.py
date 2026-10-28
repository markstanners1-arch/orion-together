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
css = (R / '_css.css').read_text(encoding='utf8')

def page(title, desc, body, script=''):
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="fonts/fonts.css">
<style>{css}</style>
</head>
<body>
{body}
{script}
</body>
</html>
'''

out = {
    'index.html': page('One sky, together',
                       'A community astrophotography project: many telescopes, one picture, credited to everyone who took part.',
                       body, (R / '_script.html').read_text(encoding='utf8')),
    # served at /spec (GitHub Pages maps /spec to spec.html)
    'spec.html': page('Submission spec · One sky, together',
                      'What to shoot and send for the Orion project: target, settings, files, folder names and how to upload.',
                      (R / 'spec_body.html').read_text(encoding='utf8')),
}
for name, html in out.items():
    (R / name).write_text(html, encoding='utf8')
    print('wrote', name, len(html))
