import re

def print_value(cnt, headTag, tailTag, content):
    cnt = cnt + 1
    head, _ = headTag.span()
    tail, _ = tailTag.span()
    print("=========" + str(cnt) + "==============")
    print(content[head:tail + 4])
    # text value
    pattern = re.compile("<.*?>")
    txt = re.sub(pattern, '', content)
    print("value:" + txt)
    # href value
    match = re.search(r'href=[\'"]?([^\'" >]+)', content)
    if match:
        print("href value:"+match.group(1))

def read_file(path):
    with open(path, 'rt', encoding='UTF8') as file:
        cnt = 0
        buf = []
        headFlag = False
        for line in file:
            line = line.strip()
            aHeadTag = re.search("<a", line)
            aTailTag = re.search("</a>", line)
            if aHeadTag != None and aTailTag !=None:
                print_value(cnt, aHeadTag, aTailTag, line)
            elif aHeadTag != None and aTailTag == None:
                buf.append(line)
                headFlag = True
            elif aHeadTag == None and aTailTag != None:
                buf.append(line)
                content = ''.join(buf)
                nHeadTag = re.search("<a", content)
                nTailTag = re.search("</a>", content)
                print_value(cnt, nHeadTag, nTailTag, content)
                buf = []
                headFlag = False
            elif headFlag == True:
                buf.append(line)


if __name__ == '__main__':
    read_file('week03\\bootstrap_example.html')