import wikipediaapi
import warnings
import urllib3

# Warning抑制
warnings.simplefilter(
'ignore', urllib3.exceptions.InsecureRequestWarning)    

api = wikipediaapi.Wikipedia(
    language='ja',
    proxies={
        'http': 'proxygate2.nic.nec.co.jp:8080',
        'https': 'proxygate2.nic.nec.co.jp:8080'
        },
    verify=False
)

page = api.page('るろうに')
print("Page - Exists: %s" % page.exists())

if page.exists():
    print(f'Page Title = {page.title}')
    print(f'Page Summary = {page.summary}')
    print(f'Page url-full = {page.fullurl}')
    print(f'Page url-canonicalurl = {page.canonicalurl}')
