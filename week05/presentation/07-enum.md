# 열거형 지원

Created: July 4, 2021 1:42 PM
Tags: enum

✔목차

# **enum이란?**

⇒ 서로 관련이 있는 **여러개의 상수의 집합**을 정의할 때 사용하는 모듈(단, 파이썬 3.4 버전 이후부터 사용가능)

## enum의 특징및 사용방법

- 열거형은 class문법을 사용하여 작성된다

    ```python
    from enum import Enum

    class Color(Enum) :
    	RED = 1
    	GREEN = 2
    	BLUE = 3
    ```

- 멤버값은 아무 것(int, str...)이나 될 수 있다.
- enum은 name과 value속성으로 접근 가능하다

    ```python
    from enum import Enum

    class Color(Enum) :
    	RED = 1
    	GREEN = 2
    	BLUE = 3

    print(Color.RED)        # 출력 : Color.RED
    print(Color.RED.value)  # 출력 : 1 
    print(Color.RED.name)   # 출력 : RED
    ```

- 순회가 가능하기 때문에 for문으로 모든 상수를 쉽게 확인 가능하다

    ```python
    from enum import Enum

    class Color(Enum) :
    	RED = 1
    	GREEN = 2
    	BLUE = 3
      PINK = 4
      ORANGE = 5
      PURPLE = 6

    for color in Color :
    	print(color)

    # 출력
    # Color.RED
    # Color.GREEN
    # Color.BLUE
    # Color.PINK
    # Color.ORANGE
    # Color.PURPLE
    ```

- 단, 이름이 같은 열거형 멤버가 중복되면 안된다.(value는 상관없다)
- 열거형 값이 아닌 값과의 비교(동등비교만 가능)는 항상 false

    ```python
    Color.BLUE == 2  # 출력 : False
    ```

- 멤버는 해시도 가능하므로 딕셔너리와 집합에도 사용할 수 있다.

    ```python
    apples = {}
    apples[Color.RED] = 'red delicious'
    apples[Color.GREEN] = 'granny smith'
    apples == {Color.RED: 'red delicious', Color.GREEN: 'granny smith'}
    # 출력 : True
    ```

## 열거형 멤버의 어트리뷰트에 접근하기

1. 만약 Color Enum클래스에 어떤 색깔이 들어가있는지 모르는 경우
2. name으로 열거형 멤버에 접근
3. 열거형 멤버가 있는데 name이나 value가 필요한 경우

```python
# 1.
Color(1)     # 출력 : <Color.RED : 1>

# 2.
Color['RED'] # 출력 : <Color.RED : 1>

# 3.
member = Color.RED
member.name  # 출력 : 'RED'
member.value  # 출력 : 1
```
