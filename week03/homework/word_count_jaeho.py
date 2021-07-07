import re

f = open("../wiki_python.txt", "r")
word = "\n".join(f.readlines())
f.close()

r = re.compile(r"[^\s]+"
,re.MULTILINE | re.VERBOSE)

result = r.findall(word)
data = dict()
for i in result:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1

# print(my_dic)

soreted_answer = sorted(data.items(), key = lambda x: x[1], reverse=True)

for i in range(10):
    print(soreted_answer[i])


#  re도 O(n), iter 순회도 O(n) 이므로 O(n) 의 시간복잡도로 해결 됩니다.