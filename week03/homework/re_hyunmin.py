import re

with open('../bootstrap_example.html', 'r', encoding='UTF-8') as f:
    raw_data = f.read()
    
    pattern = "<a.+?href\=\"(.+?)\".*>(.*?)</a>"
    p = re.compile(pattern)
    matched = p.findall(raw_data)
    
    for tag in matched:
        print(f"{tag[0]}, {tag[1]}")