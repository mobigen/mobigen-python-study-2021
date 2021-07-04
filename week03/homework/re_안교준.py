import requests
import re

a_re = re.compile('<a.+</a>')
href_re = re.compile('href="(.*?)"')
value_re = re.compile('>.+</')
html = requests.get('https://raw.githubusercontent.com/mobigen/mobigen-python-study-2021/master/week03/wiki_python.html')

for text in a_re.findall(html.text):
    output = '{1}, {0}'
    href = href_re.search(text)
    value = value_re.search(text)
    if href and value:
        href = href.group().replace('href="', '').replace('"','')
        value = value.group().replace('>', '').replace('</', '')
        print(output.format(href, value))

