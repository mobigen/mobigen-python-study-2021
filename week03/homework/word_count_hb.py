import re

def word_count(textList):
    r = dict()
    for i in textList:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    return r   

if __name__ == "__main__" :
    f = open('../wiki_python.txt','r')

    data = f.read().replace('\n', ' ')
    words = re.findall(r'\S+', data)

    counts = word_count(words)
    sorted_words = sorted(counts.items(),key=lambda x:x[1],reverse=True)
    
    for i in range(10):
        print(sorted_words[i])




