# 대안 repr() 구현

Created: July 4, 2021 1:42 PM
Tags: repr(), reprlib

✔목차

# **reprlib모듈이란?**

결과 문자열의 **크기에 제한**이 있는 객체 표현을 생성하는 수단을 제공하는 라이브러리

### **repr(내장)함수란?**

어떤 객체의 출력될 수 있는 표현을 문자열의 형태로 반환해주는 함수

```python
import math

print(repr(3))        # 3
print(repr([1,2,3]))  # [1, 2, 3]
print(repr(math))     # <module 'math' (built-in)>
```

### **repr함수는 어디에 사용될까?**

- 주로 디버거에서 사용된다.

    즉, 파이썬에서 해당 객체를 만들 수 있는 문자열로 출력된다

 **내장 repr()함수                                                                                   vs      reprlib의 repr()함수**

```python
print(repr(set('appleisdelicousandverysweet')))

# 출력결과
#{'s', 'd', 'u', 'y', 'v', 'l', 'a', 'r', 'e', 
#          'w', 't', 'p', 'o', 'i', 'n', 'c'}
```

```python
import reprlib

print(reprlib.repr(set('appleisdelicousandverysweet')))

# 출력결과
#{'a', 'c', 'd', 'e', 'i', 'l', ...}
```

- **str과 repr의 차이는 무엇일까?**

    ```python
    s = "Hello, World!"

    print(str(s))   #  Hello, World!
    print(repr(s))  # 'Hello, World!'
    ```

    - str : 변수에 들어있는 값을 문자열로 출력

        ⇒ print가 인자들을 str화 해서 출력한다

        ```python
        a = 1
        b = '가'
        c = [1,2,3,4,5]

        print(a,b,c)
        # 출력
        # 1 가 [1,2,3,4,5]
        ```

    - repr: 변수에 들어있는 값을 객체로 만들 수 있는 문자열로 출력
