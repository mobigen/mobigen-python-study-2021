import re

f = open("../wiki_python.html", "r")
word = "\n".join(f.readlines())
# word =	"""<a id="top"></a>"""

f.close()
r = re.compile('''
<a.+?href=               # a태크로 시작 사이에 다른 속성이 들어가는것도 포함하고 href= 포함
\"(.+?)\"               # 쌍따옴표 이스케이프 처리, 탐욕을 억제하여 두개의 쌍따옴표 사이이 path 그루핑 
.*?>                    # 다른 속성이 들어가는것들 포함하고 a태그를 닫는것 포함
(.*?)</a>               # > </a 사이에 value가 있다고 가정, 탐욕을 억제하여 그루핑
''', re.MULTILINE|re.VERBOSE|re.DOTALL)

data = r.findall(word)
# print(data)


for i in data:
    print(i)

print("총 데이터의 갯수: " + str(len(data)))