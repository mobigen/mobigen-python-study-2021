import os

path = os.getcwd()
with open(f'{path}/wiki_python.txt', encoding='utf-8') as f:
    file = f.read()
    words = file.split()
    
word_count = {}
count = 0

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

rank  = sorted(word_count.items(), key=lambda x : x[1], reverse=True)

for i in range(10):
    print(rank[i])