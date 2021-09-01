import re

tmp_list = []

with open('../wiki_python.html', 'r', encoding='UTF-8') as f:
    for data in re.finditer(r'\<a.+href\=\"([^\"]*).*\>(.*)\</a\>', f.read()):
        tmp_list.append([data.group(2), data.group(1)])

    for i in tmp_list:
        print(i)
