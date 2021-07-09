# 정규표현식이란 ?

복잡한 문자열을 처리할떄 사용하는 기법으로 . 모든 언어에서 공통으로 사용됨


검사하는 수식들이 있음

## []

- [] 대괄호 사이에 있는 문자와 매치 하는지 
- [a-c]하이픈을 사용하여 From to 표현 가능

- [abc]
- a와 일치 
- before b 속해있으니 매치 
- dude 어느 하나도 포함하고 있지 않으니 매치 않음
- [a-c] = [abc] [0-5] = [012345]

## Dot(.)
  - 줄바꿈(\n)을 제외한 모든 문자와 매치함
  - aab 는 가운데 문자 "a" 가 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치  
  - a0b 가운데 "0"가 모든 문자를 의미하는 "." 일치하므로 정규식과 매치 
  - abc ab사이에 문자가 없으므로 매치하지 않음 

## 반복(*)
- ca*t 
- 여러번 반복되는 표현식 
- ct 는 a가 0번 반복되도 매치 
- cat는 a가 0번 이상 반복되어 매치 (1번 반복)
- caaat는 a가 0번 이상 반복되어 매치 (3번 반복)

## 반복 (+) 
- ca+t
- 반복을 나타내는 + 기호 
- *와 차이점은 ct는 a가 0번 반복되기 떄문에 매치하지 않음 
- cat는 a가 1번 반복됭 매치 (1번반복)
- caat는 a가 1번 이상 반복되어 매치 (3번반복)

## 반복({m,n},?)
  - 최소, 최대 , 횟수
  
  - ca{2}t
  - cat는 a가 1번만 반복되어 매치가 되지 않고 
  - caat는 a가 2번 반복되어 매치가 됨
  - ca?t : ? ={0,1} 와 같은 표현

  

# RE 모듈

- 정규표현식을 지원하는 re 모듈 complie 하여 패턴객체를 생성하여 원하는 문자열에 비교를 해볼수 있음. 




```python
import re
p = re.compile ('[a-z]+') # 정규 표현식 패턴 객체를 만든다  a-z까지 문자열이 1번이상 반복되는 문자열을 찾는다 
```

## match: 문자열의 가장 앞에서 일치하는 패턴을 찾기


```python
import re 
p = re.compile('[a-z]+') #a ~ z 까지 반복되는지 
m = p.match('python') #검사하고자 하는 객체 
print(m)
n = p.match('3 python') #검사하고자 하는 객체  매치가 안될경우 None으로 나옴
print(n)
```

    <re.Match object; span=(0, 6), match='python'>
    None
    

## search: 문자열에서 가장 첫번째로 일치하는 패턴 찾기
 - match와 다르게 첫번째개 맞지 않아도 패턴을 찾아준다 


```python
import re 
p = re.compile('[a-z]+') #a ~ z 까지 반복되는지 
m = p.search('3 python') #찾고자 하는 객체 
print(m)

```

    <re.Match object; span=(0, 6), match='python'>
    

## findall: 일치하는 패턴을 모두 찾기


```python
import re
p = re.compile('[a-z]+') #a ~ z 까지 반복되는지 
m = p.findall('life is short') # 매칭되는것을 찾아서 리스트로 리턴
print(m)
```

    ['life', 'is', 'short']
    

## finditer: iterator 객체가 출력


```python
import re
p = re.compile('[a-z]+') #a ~ z 까지 반복되는지 
m = p.finditer('life is short') 
for r in m:
    print(r)
```

    <re.Match object; span=(0, 4), match='life'>
    <re.Match object; span=(5, 7), match='is'>
    <re.Match object; span=(8, 13), match='short'>
    

# 실습

## 이메일 유효성 검사

- 이메일 정규 표현식 : [a-zA-Z0-9._+-]+@[0-9a-z]+\.[0-9a-z]+


```python
import re
a = re.compile("[a-zA-Z0-9._+-]+@[0-9a-z]+\.[0-9a-z]+")     # email 유효성 검사      
b = a.match("mobigen123@naver.com")
c = a.match("abcfdfdf")
print(b)
print(c)


```

    <re.Match object; span=(0, 20), match='mobigen123@naver.com'>
    None
    

## 주민등록번호 뒷자리 바꾸기

- 주민등록번호 정규 표현식 : [0-9]{6}\-[0-9]{7}, [a-zA-Z0-9._+-]+@[0-9a-z]+.[0-9a-z]+


```python
import re 
s ="주민등록번호는 750511-1010101 "
p = "[0-9]{6}\-[0-9]{7}"          
print(re.findall(p, s))
p = "([0-9]{6})\-([0-9]{7})"      #그룹핑
print(re.findall(p, s))
re.sub(p, "\g<1>-********", s)

```

    ['750511-1010101']
    [('750511', '1010101')]
    




    '주민등록번호는 750511-******** '



## 핸드폰 번호 뒷자리 4자리 바꾸기 

- 핸드폰번호 정규 표현식 : "(\d+)[-](\d+)[-](\d+)", "(\d{2,3})[-](\d{4})[-](\d{4})"


```python
import re 
s = "저의 전화번호는 010-1234-1356 입니다"
#n = re.compile("(\d+)[-](\d+)[-](\d+)")
#n = re.compile("(\d{2,3})[-](\d{4})[-](\d{4})")
print(n.findall(s))

re.sub(n,"\g<1>-\g<2>-****", s )
```

    [('010', '1234', '1356')]
    




    '저의 전화번호는 010-1234-**** 입니다'




```python

```
