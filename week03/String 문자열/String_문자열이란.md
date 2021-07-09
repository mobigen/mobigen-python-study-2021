# 문자열 이란? 


- **문자열(String)**
    - Quatation안에 들어있는 '문자', '단어', '숫자' 등으로 구성된 집합 
    - 시퀀스 자료형 (Sequence Data type) 
    - 파이썬의 문자열의 immutable한 자료형으로 변경이 불가능합니다.  



```python
s = "String"
print(s) #전체를 출력하는 것
print(s[0]) #하나씩 인덱스 0번째 출력 
```

    String
    S
    


```python
s= "문자열" #파이썬은 unicode를 지원하기 떄문에 각국 나라의 언어를 다룰수 있다
print(s)
print(s[0])
```

    문자열
    문
    


```python
s ="12.1"
print(s)
```

    12.1
    


```python
s= 'python'  #python에 ㅑ를 넣어준다고해서 iython이 되지 않는다 
s[0] = 'i'
print(s)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-89-49c438991c91> in <module>
          1 s= 'python'
    ----> 2 s[0] = 'i'
          3 print(s)
    

    TypeError: 'str' object does not support item assignment


## 문자열 생성 : 만들기는 4가지 방법이 있음 

- 작은 따음표(') 이용
- 큰 따음표 (") 이용
- 작은 따음표 3개 (''') 이용 
- 큰 따음표 3개 (""")이용

## Multiline 생성 

- 여러줄이 있는 문자열 생성 이스케이프 문자(\n)를 이용하여 여러 줄이 있는 문자열 생성 가능
- ***작은 따음표 3개(''') 또는 큰 따음표 3개(""")를 이용하여 여러줄이 있는 문자열 생성***
    


```python
text='''  
가나다라
마바사하
자카타파하
'''
print(text) #엔터한 값이 적용된 여러줄의 문자열이 생성된다 

text = "가나다라\n마바사하\n자카타파하"
print(text)
```

      
    가나다라
    마바사하
    자카타파하
    
    가나다라
    마바사하
    자카타파하
    


```python
print('hello')
print("파이썬은 공부하자")
print('''파이썬 심플하다 ''')
print("""파이썬 문자 처리가 뛰어나다 """)
```

    hello
    파이썬은 공부하자
    파이썬 심플하다 
    파이썬 문자 처리가 뛰어나다 
    

## 따음표가 있는 문자열 생성
- 문자열에 작은따음표가 있을 경우, 큰 따옴표로 둘러싸서 표현
- 문자열에 큰 따음표가 있을 경우, 작은 따음표로 둘러싸서 표현
- ***이스케이프 코드 \(백슬래시) 를 이용하여 작은따음표(')와 큰 따음표(")를 문자열에 포함***


```python
string = 'Python's built-in string classes'
print(String)
```


      File "<ipython-input-42-2d2390044304>", line 1
        string = 'Python's built-in string classes'
                         ^
    SyntaxError: invalid syntax
    



```python
string = "Python's built-in string classes"
print(string)
```

    Python's built-in string classes
    


```python
string = "나는 "오늘 공부를한다" 라고 말한다"
print(string)
```


      File "<ipython-input-12-6ffb2ec0fa69>", line 1
        string = "나는 "오늘 공부를한다" 라고 말한다"
                      ^
    SyntaxError: invalid syntax
    



```python
string = "나는 \"날씨가 좋다\" 라고 말한다"
print(string)
```

    나는 "날씨가 좋다" 라고 말한다
    


```python
string = 'Python\'s built-in string classes'
print(string)
```

    Python's built-in string classes
    

# 문자열 인덱싱과 슬라이싱

## 문자열 인덱싱 [index]
- 문자열 리스트처럼 문자 하나하나 상대적인 주소를 가짐
- 문자열에 있는 요소 하나하나에 접근하는 방법
- 고유 번호 주소를 사용해 할당된 값을 가져오는 인덱싱을 사용
- **파이썬은 다른 언어와 다르게 음수로도 접근을 허용함**

String    
012345    
**-6-5-4-3-2-1**
    
  

s = "string"   #S의 -6번째 문자를 출력해서 해당 인덱스의 문자를 출력할수 있다. 
print(s)
print(s[-6])

## 문자열 슬라이싱[시작 index:끝 index]
- 문자열을 자른다는 의미 
- **인덱싱을 통해서 문자열을 자를수 있음** 
- 문자열의 주소를 이용하여 문자열을 조각(부분)을 추출 

- **지난주 다룬 리스트에서 인덱싱과 동일하게 문자열에서도 같은 원리로 추출이 가능**


```python
s = "문자열의 주소를 이용하여 문자열 조각 추출 "
print(s[:5]) # 맨 앞에서부터 뒤 index까지 말함
print(s[5:]) #앞 inedex에서부터 문자열 맨 뒤까지 말함
print(s[:]) #문자열 맨 앞에서부터 맨 뒤까지 말함
```

    문자열의 
    주소를 이용하여 문자열 조각 추출 
    문자열의 주소를 이용하여 문자열 조각 추출 
    


```python
My_list = [1,2,3,4]
print(My_list[1])
```

    2
    

# 문자열 연산 (연결, 반복, 길이)

## 문자열 더하기 곱하기 

- **새롭게 이어진 문자열이 생성됩니다.**
    + "+" 연산자를 사용하여 문자열 **연결** 
    * "*" 연산자를 사용하여 문자열 **반복**


```python
s1="python"
s2="easy"
print(s1+s2) #새롭게 이어진 문자열 생성
print(s1*3)  #문자열 N반복 문자열 생성 
print(s1*0)  #0을 곱하게 되면 0번이기 떄문에 빈 문자열이 나옴
```

    pythoneasy
    pythonpythonpython
    
    

## 문자열 길이 구하기 (length)
- 문자열 길이 구하려면 내장함수인 len(문자열)을 이용하여 문자열 길이 구할 수 있음


```python
s = "string "
print(len(s)) #내장함수
print(len(s*3))
```

    7
    21
    

# 문자열 String Processing

## 문자열 목록

- 파이썬은 문자열 형식을 목록으로 만들어서 제공하고 있음 


```python
import string
print(string.digits) # 십진수 0 ~ 9 까지 출력
print(string.ascii_letters) # 영어 알파벳 소문자, 대문자 모두를 출력
print(string.ascii_lowercase) # 영어 소문자를 출력
print(string.hexdigits) # 16진수 출력
print(string.octdigits) # 8진수 출력
print(string.punctuation) # 특수 문자 출력
print(string.printable) # digits, ascii_letters, punctuation, whitespace 의 조합
print(string.whitespace) # 공백으로 간주하는 모든 문자,  스페이스, 탭, 줄 바꿈, 캐리지 리턴, 세로 탭 및 폼 피드 문자가 포함
```

    0123456789
    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    abcdefghijklmnopqrstuvwxyz
    0123456789abcdefABCDEF
    01234567
    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	
    
     	
    
    


- 문자열 형식으로 출력되기 때문에 아래와 같이 원하는 길이만큼 인덱스를 이용하여 자를 수 있음


```python
import string
print(string.ascii_lowercase)
print(type(string.ascii_lowercase))
print(list(string.ascii_lowercase[:10]))
```

    abcdefghijklmnopqrstuvwxyz
    <class 'str'>
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    

# 문자열 포맷팅(String Formatting) 방식


## 기본 형식
- % formatting: 포맷 코드를 사용하는 오래된 스타일의 formatting 방법
- String formatting: 새로은 스타일의 formatting 방법
- f-string: Python 3.6 이상에서 사용할 수 있는 새로운 스타일의 formatting 방법

### [참조] 문자열 포맷 코드 String Format code
- 문자열 포맷팅에서 사용할 수 있는 다양한 포맷 코드
- 정렬, 공백, 소수점 포맷 
- 포맷 문자 앞에 숫자는 길이를 의미
    
    
| 코드 | 설명 |
| ------ | ------ |
| %s | 문자열 |
|%c  | 문자열 |
|%c  | 문자열 |
|%d  | 정수|
|%f |  부동소수|
|%o  | 8진수 |
|%x  | 16진수 |
|%%  | 문자% |






```python
temperature = 202
measure = 'Fahrenheit'
print('Water boils at %d degrees %s' % (temperature, measure))     # 1
print('Water boils at {} degrees {}'.format(temperature, measure)) # 2
print(f'Water boils at {temperature} degrees {measure}')           # 3
```

    Water boils at 202 degrees Fahrenheit
    Water boils at 202 degrees Fahrenheit
    Water boils at 202 degrees Fahrenheit
    


```python
age = 30
f'나는 {age+1}살 입니다.'

```




    '나는 31살 입니다.'



- 위치로 인자 액세스:
    - 두개 이상의 값을 넣을 경우에 {0), {1} 인덱스 항목을 format의 함수의 입력값으로 순서에 맞게 바꿔줌
    - 인덱스 번호에 따라 format() 함수의 각 값들이 매핑이 가능


```python
print("나는 사과가 {0}개 있다".format(2))
print("나는 사과가 {0}개 있다".format("두"))
print("나는 {0}가 {1}개 있다".format("사과",2)) #인덱스 번호에 따라 포맷에 정의된 값이 입력되어 들어온다 
```

    나는 사과가 2개 있다
    나는 사과가 두개 있다
    나는 사과가 2개 있다
    

## Padding(공백), Aligning(정열)


```python
string = 'test'
print('%10s' % (string)) #공백 왼쪽, 정렬 오른쪽
print('{:>10}'.format(string))
print(f'{string:>10}')
```

          test
          test
          test
    


```python
string = 'test'
print('%-10s' % (string))  #공백 오른쪽, 정렬 왼쪽
print('{:10}'.format(string)) # (String formatting과 f-string에서 :뒤에 <를 입력해도 되고 생략해도 됩니다.)
print(f'{string:10}') # (String formatting과 f-string에서 :뒤에 <를 입력해도 되고 생략해도 됩니다.)
```

    test      
    test      
    test      
    


```python
string = 'test'
print('{:*>10}'.format('test'))
print(f'{string:*>10}')

print('{:*<10}'.format('test'))
print(f'{string:*<10}')
```

    ******test
    ******test
    test******
    test******
    

- 가운데 정렬 ^ 입니다.


```python
string = 'test'
print('{:^10}'.format('test'))
print(f'{string:^10}')

print('{:*^10}'.format('test'))
print(f'{string:*^10}')
```

       test   
       test   
    ***test***
    ***test***
    

## 문자열을 자르기 


```python
string = 'xylophone'
print('%-.5s' % (string))
print('{:.5}'.format(string))
print(f'{string:.5}')
```

    xylop
    xylop
    xylop
    

## 숫자 출력하기  |%f |  부동소수| float은 소수 6자리까지만 표현


```python
number = 3.141592653589793
print('%f' % (number))
print('{:f}'.format(number))
print(f'{number:f}'.format(number))

print(f'{number}')
```

    3.141593
    3.141593
    3.141593
    3.141592653589793
    


```python
number = 3.141592653589793
print('%.2f' % (number))
print('{:.2f}'.format(number))
print(f'{number:.2f}')
```

    3.14
    3.14
    3.14
    


```python
number = 3.141592653589793
print('%.3f' % (number))
print('{:.3f}'.format(number))
print(f'{number:.3f}')
```

    3.142
    3.142
    3.142
    

## 이름으로 인자 출력하기


```python
d = {'name': '문과생 주디', 'year':'13'} #딕셔너리에서 f를 활용한 포맷팅
f"안녕하세요 저는 {d['name']}입니다. 나이는 {d['year']}입니다."
```




    '안녕하세요 저는 문과생 주디입니다. 나이는 13입니다.'



## 쉼표를 천 단위 구분자 사용


```python
'{:,}'.format(1234567890)
```




    '1,234,567,890'



## 백분율 표현


```python
points = 19
total = 22
'Correct answers: {:.2%}'.format(points/total)
```




    'Correct answers: 86.36%'



# 문자열 메소드 함수

## 문자열 변환(변경)

- **capitalize() 첫문자를 대문자로 변경**
- **title() 각 단어의 첫글자를 대문자로 변경** 




- **replace(old, new) 문자열 특정 부분을 변경 대체**
- **join 리스트 같은 iterable 인자를 전달하여 문자열로 연결, 파이썬에서 join () 함수 를 사용 하면 목록의 모든 문자를 결합 할수 있음**



```python
s1 = 'this is my blog. 123 456'
s2 = "THIS IS MY BLOG. 123 456"

r1 = s1.capitalize() #첫문자를 대문자로 변경
print(r1)
r2 = s1.title() #각 단어의 첫글자를 대문자로 변경 
print(r1)
r3 = s2.title() #첫문자를 대문자로 변경
print(r2)
r4 = s1.title() #각 단어의 첫글자를 대문자로 변경 
print(r2)
```

    This is my blog. 123 456
    This is my blog. 123 456
    This Is My Blog. 123 456
    This Is My Blog. 123 456
    


```python
a = 'I Love Python'

a.replace('Python', 'R')

```




    'I Love R'




```python
str = ""
str1 = ( "geeks", " ", "for"," ","geeks")
str.join (str1) 
```




    'geeks for geeks'



## string.capwords 

- str.capitalize() 를 사용하여 각 단어의 첫 글자를 대문자로 만들고, 이렇게 만들어진 단어들을 str.join() 을 사용하여 결합
- 구분 인자 sep 가 없거나 None 이면, 연속된 공백 문자는 단일 스페이스로 바뀌고 앞뒤 공백이 제거됨
- 그렇지 않으면 sep 가 단어를 나누고 합치는 데 사용됨


```python
import string

mystring = "hey!   what's up?"
print(mystring)
print(string.capwords(mystring))
```

    hey!   what's up?
    Hey! What's Up?
    


```python
import string # imports string module
  
sentence = 'Python is one of the best programming languages.'
  
# sep parameter is 'g'
formatted = string.capwords(sentence, sep = 'g')
print('When sep = "g"', formatted)
  
# sep parameter is 'o'
formatted = string.capwords(sentence, sep = 'o')
print('When sep = "o"', formatted)
```

    When sep = "g" Python is one of the best progRamming langUagEs.
    When sep = "o" PythoN is oNe oF the best proGramming languages.
    

## 문자열 횟수 Count

- count()  문자열 내부에서 특정 문자가 등장하는 횟수를 알려줌
- 특정 단어(문자열)의 수를 구함(**없으면 0을 반환**)

- **string.count(x)** :문자열 전 범위에서 (x) 문자가 등장하는 횟수를 반환하는 메서드
- **string.count(x, start)** :문자열 start index부분에서부터 시작해서 문자열 끝가지 x가 등장하는 횟수를 반환하는 메서드 
- **string.count(x, start, end)** #문자열 start index 부분에서 end index 부분까지 문자열에서 x가 등장하는 횟수를 반환하는 메서드


```python
a = "python is easy easy easy"
print(len(a))

```

    24
    


```python
a = "python is easy easy easy"
r1 = a.count('is')  #전체 문자열에서 문자 찾기 
print(r1)
r2 = a.count('easy') #전체 문자열에서 문자 찾기 
print(r2)
r3 = a.count('easy',9,20) #Start index 9 ~ end index 20 에서 문자 찾기 
print(r3)
r4 = a.count('not') #없으면 0을 반환
print(r4)
```

    1
    3
    2
    0
    

## 문자열 검색 

- find() 특정 단어를 찾아 인덱스를 리턴 (없으면 -1 반환)
- rfind() 뒤에서부터 특정 단어를 찾아 인덱스를 리턴
- index() -  find()와 기능 동일하나, 매개변수로 입력한 문자열이 없으면 ValueError 발생
- rindex() - index()와 기능 동일하나, 뒤에서 부터 매개변수의 문자열이 있는지를 찾음


```python
a = 'I Love Python'

f1 =a.find('o')
print(f1)

f2=a.find('k') # 문자열에 매개변수로 입력한 문자열이 있는지를 앞에서 부터 찾아 index 반환, 없으면 '-1' 반환
print(f2)
```

    3
    -1
    


```python
a = 'I Love Python'

f3= a.rfind('o') # 문자열에 매개변수로 입력한 문자열이 있는지를 뒤에서 부터 찾아 index 반환, 없으면 '-1' 반환
print(f3)
```

    11
    


```python
a = 'I Love Python'

a.index('k') # 문자열이 없으면 ValueError 발생
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-120-59a8509fda80> in <module>
          1 a = 'I Love Python'
          2 
    ----> 3 a.index('k') # 문자열이 없으면 ValueError 발생
    

    ValueError: substring not found



```python
'I am a boy'.rindex('y')
```




    9



## 문자열 분리 (나누기)

- **partition() 전달한 문자로 문자열 나눔(분리), 결과는 튜플 (구분자도 포함)**
- rpartition() 뒤에서 부터 전달한 인자로 문자열을 나눔
- **split() 문자열을 구분자(구분기호 : delimiter, separator) 기준에 따라 나누기, 전달한 문자로 문자열을 나눔, 결과는 리스트 (구분자 포함 안됨)**
- rsplit() 뒤에서 부터 전달한 문자로 문자열을 나눔
- splitliness() 라인 단위로 문자열을 나눔 


```python
a = "Python is very good!!"
a.partition('is')
```




    ('Python ', 'is', ' very good!!')




```python
x = 'haha: hoho: hihi'

x.split(sep =':') # 결과값은 리스트로 반환. default 구분자 는 공백 Space이다 



```




    ['haha', ' hoho', ' hihi']



# 두 문자열 비교하기 (difflib) 라이브러리 

- HTML 및 문맥(context)과 통합(unified) diff를 비롯한 다양한 형식의 파일 차이에 관한 정보를 비교 생성 


## SequenceMatcher : 문자열의 유사성 검사
 - - 파이썬 표준 라이브러리인 difflib의 SequenceMatcher를 사용해서 두 개의 문자열의 유사성을 수치화할 수 있음


```python
from difflib import SequenceMatcher

str1 = 'abc'
str2 = 'abc'

ratio = SequenceMatcher(None, str1, str2).ratio()
print(ratio) # 동일한 두 개의 문자열에 대해 1.0이라는 결과를 출력합니다.
```

    1.0
    


```python
from difflib import SequenceMatcher

str1 = 'abcd'
str2 = 'dabc'

ratio = SequenceMatcher(None, str1, str2).ratio()
print(ratio) # ‘abcd’와 ‘dabc’는 0.75만큼 유사함을 알 수 있습니다.
```

    0.75
    


```python
from difflib import SequenceMatcher

str1 = 'abcd'
str2 = 'efgh'

ratio = SequenceMatcher(None, str1, str2).ratio()
print(ratio) # ‘abcd’와 ‘efgh’의 유사성을 확인해보면, 0.0을 출력합니다. 유사함이 없음을 알수 있습니다.
```

    0.0
    

## get_close_matches : cutoff() 인자 값을 사용하여 최상에 단어 일치 


```python
from difflib import get_close_matches

str1='abcd'
word_lists=["acdefgh", "abcd", "adef","cdea"]
matches = get_close_matches(str1, word_lists, n=2, cutoff=0.3) #2개 Arg, 최소 유사상 cutoff
print(matches)[RE .md](https://github.com/hyesunjang1201/mobigen-python-study-2021/files/6788690/RE.md)

```

    ['abcd', 'acdefgh']
    

## Differ : 문장간에 차이 

- '- ' 시퀀스 1에만 있는 줄

- '+ ' 시퀀스 2에만 있는 줄

- '  ' 두 시퀀스에 공통인 줄

- '? ' 두 입력 시퀀스에 없는 줄


```python
from difflib import Differ

diff = difflib.Differ()

s = "abdc"
b = "acb"

result = list(diff.compare(s,b))
print(result)

```

    ['  a', '+ c', '  b', '- d', '- c']
    


```python
from difflib import Differ

text1= '''
hello world,
we like python.'''.splitlines()

text2='''
hello world,
we like python coding.'''.splitlines()

#어떤 문장이 유사하고 유사하 지 않은지 알수 있을까?

dif= Differ()
df=list(dif.compare(text1, text2))
        
from pprint import pprint 

pprint(df)
        
```

    ['  ',
     '  hello world,',
     '- we like python.',
     '+ we like python coding.',
     '?               +++++++\n']
    

# 문자열 줄바꿈 textwrap.wrap
 - textwrap.wrap은 문자열을 특정길이에 맞게 줄바꿈(wrapping)할 수 있는 표준 라이브러리 
 - 문자열 래핑은 문자열이 너무 길어질 경우 특정 길이에서 줄바꿈을 하려고 할때 필요함


```python
long_text = 'Life is too short, you need python. ' * 10
long_text
'Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. Life is too short, you need python. '

# long_text를 70바이트 길이로 줄바꿈 하시오.

import textwrap

long_text = 'Life is too short, you need python. ' * 10

result = textwrap.wrap(long_text, width=70)  # 긴 문자열을 매개변수 width로 전달한 70바이트 길이만큼 잘라서 리스트로 리턴
print(result)
```

    ['Life is too short, you need python. Life is too short, you need', 'python. Life is too short, you need python. Life is too short, you', 'need python. Life is too short, you need python. Life is too short,', 'you need python. Life is too short, you need python. Life is too', 'short, you need python. Life is too short, you need python. Life is', 'too short, you need python.']
    

- 고정폭 문자열을  fill()을 통해  다음의 줄 표현 함
- textwarp.fill은 '\n'.join(result) 을 포함하고 있음


```python
import textwrap

long_text = 'Life is too short, you need python. ' * 10

result = textwrap.fill(long_text, width=70)
print(result)
```

    Life is too short, you need python. Life is too short, you need
    python. Life is too short, you need python. Life is too short, you
    need python. Life is too short, you need python. Life is too short,
    you need python. Life is too short, you need python. Life is too
    short, you need python. Life is too short, you need python. Life is
    too short, you need python.
    

# unicodedata
 - 유니코드 문자에 대한 문자 속성을 정의하는 유니코드 문자 데이터베이스(UCD – Unicode Character Database)에 대한 액세스를 제공
 - 각 unicode에 대해 어떤 category을 갖는지 확인해서 제거할 수 있음. 


```python
import unicodedata
unicodedata.lookup('LEFT CURLY BRACKET') # 대소문 문자를 취하지 않는 유니코드 문자 반환


```




    '{'




```python

unicodedata.name('/') #인자를 유니코드로 취하고 대문자 이름을 반환

```




    'SOLIDUS'




```python
unicodedata.decimal('9') #10진수 값을 정수로 반환 


```




    9




```python
unicodedata.category('A')  # 'L'etter, 'u'ppercase #문자에 지정된 일반 카테고리 를 문자열로 반환 
```




    'Lu'




```python
unicodedata.bidirectional('\u0660') # 'A'rabic, 'N'umber  #텍스트에서 Bidirectional은 하나의 텍스트가 두 가지 방향성
```




    'AN'




```python

```
