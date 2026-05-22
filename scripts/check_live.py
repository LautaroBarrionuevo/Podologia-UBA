import urllib.request

urls = [
    'https://podologia-uba.vercel.app/',
    'https://podologia-uba.vercel.app/pages/contacto.html',
    'https://podologia-uba.vercel.app/pages/empleo.html',
    'https://podologia-uba.vercel.app/pages/login-medico.html',
    'https://podologia-uba.vercel.app/pages/login-paciente.html',
]
css_url = 'https://podologia-uba.vercel.app/assets/css/style.css'


def analyze(html):
    h = html.lower()
    return {
        'has_viewport': ('<meta name="viewport"' in h) or ('name="viewport"' in h),
        'has_title': ('<title>' in h and '</title>' in h),
        'has_description': ('<meta name="description"' in h),
        'html_lang': ('<html' in h and 'lang=' in h),
        'h1_count': h.count('<h1'),
        'img_count': h.count('<img'),
        'img_alt_count': h.count('alt='),
        'uses_bootstrap': ('bootstrap' in h) or ('cdn.jsdelivr' in h) or ('stackpath.bootstrapcdn' in h) or ('cdn.jsdelivr.net' in h),
        'links_css_style': ('assets/css/style.css' in h) or ('/assets/css/style.css' in h)
    }


for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            a = analyze(html)
            print('\n==', url, '==')
            print('Viewport meta:', a['has_viewport'])
            print('Title present:', a['has_title'])
            if a['has_title']:
                tstart = html.lower().find('<title>') + 7
                tend = html.lower().find('</title>')
                print(' Title:', html[tstart:tend].strip())
            print('Meta description:', a['has_description'])
            print('HTML lang attribute present:', a['html_lang'])
            print('H1 count:', a['h1_count'])
            print('Images / alt occurrences:', a['img_count'], '/', a['img_alt_count'])
            print('Bootstrap detected:', a['uses_bootstrap'])
            print('References `assets/css/style.css`:', a['links_css_style'])
    except Exception as e:
        print('\n==', url, '== FAIL', e)

# Check CSS for media queries and responsive rules
try:
    req = urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as r:
        css = r.read().decode('utf-8', errors='ignore')
        print('\n== CSS checks ==')
        print('CSS fetched:', len(css) > 0)
        print('@media queries found:', css.count('@media'))
        print('Responsive units (rem, vw, %) occurrences:', css.count('rem'), css.count('vw'), css.count('%'))
except Exception as e:
    print('\n== CSS checks == FAIL', e)
