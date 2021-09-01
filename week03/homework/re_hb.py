import re

if __name__ == "__main__" :
    f = open('../wiki_python.html','r')
    
    lines = f.read()
    
    r = re.compile('''
    <a.+?href=         
    \"(.*?)\"(.*?)>        
    (.*?)
    </a>          
    ''', re.VERBOSE)

    result = r.findall(lines)
    for i in result:
        print(i)
    print(len(result))

