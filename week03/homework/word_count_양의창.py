from collections import Counter

f = open("python_study/wiki_python.txt",'r',encoding='UTF-8')

wordDict=Counter()
words=[]
lines = f.readlines()

for line in lines:
    words.append(line.replace("\n", "").replace("\t",''))

splitword = ' '.join(words).split(' ')

for word in splitword:
    if word == '':
        pass
    else:
        wordDict[word]+=1

for w, k in wordDict.most_common(10):
    print(w+' : '+str(k))

f.close()