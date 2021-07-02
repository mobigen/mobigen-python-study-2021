from os import replace
import re, codecs

f=codecs.open('python_study\wiki_python.html','r','UTF-8')
data=f.read()
finda=re.findall("<a.*/a>",data)
href=[]
tag=[]
for atag in finda:
    hr=re.findall('href=".*?"',atag)
    tg=re.findall('>.*<',atag)
    for hre in hr:
        continue
    for atg in tg:
        continue
    result1=hre.replace('href="','').replace('"','')
    result2=atg.replace('<','').replace('>','')
    print(result1+', '+result2)

