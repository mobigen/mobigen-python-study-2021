import re


with open('../bootstrap_example.html', 'r', encoding='UTF-8') as f:
    data = f.read()

# pattern = r'\<a.+href\=\"(.+?)\".+\>(.+)\<\/a\>'
# matched = re.findall(pattern, data)
#
# for url, value in matched:
#     print(f"[{value}] is [{url}]")

pattern = r'\<a.+?href\=(?P<dquote>\")(.+?)(?P=dquote).*?\>([\s\S]+?)\<\/a\>'
matched = re.findall(pattern, data)

for _, url, value in matched:
    print(f"[{value}] is [{url}]")

print(len(matched))
