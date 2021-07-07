
import re

word_count_map = {}

def read_file(path):
    with open(path, 'rt', encoding='UTF8') as file:
        for line in file:
            arr = re.split("\\s|\\n|\\t", line)
            for word in arr:
                #word = re.sub(r'[()^\s}]','',word)
                if word == '':
                    continue
                if word in word_count_map.keys() :
                    word_count_map[word] = word_count_map[word] +1
                else:
                    word_count_map[word] = 1

    sorted_word_count_map = {k:v for k,v in sorted(word_count_map.items(), key=lambda item:-item[1])}

    top = 10

    for key in sorted_word_count_map.keys():
        print(key+':'+str(word_count_map[key]))
        top -=1
        if top <=0:
            break



if __name__ == '__main__':
    read_file('week03\wiki_python.txt')