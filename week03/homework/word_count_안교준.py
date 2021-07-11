import requests
dict = {}
html = requests.get('https://raw.githubusercontent.com/mobigen/mobigen-python-study-2021/master/week03/wiki_python.txt')
for word in list(filter(None, html.text.split(' '))):
    if(word not in dict):
        dict[word] = 0
    dict[word] += 1;

result = sorted(dict.items(), key = lambda item: item[1], reverse=True)
for i in range(0,10):
    print(result[i])
