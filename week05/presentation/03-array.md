# 효율적인 숫자 배열 array

Created: July 4, 2021 1:37 PM
Tags: array

**✔목차**

# 효율적인 숫자 배열

이 모듈은 기본적인 값의 배열을 간결하게 표현할 수 있는 객체형이다.

파이썬에서는 배열이라는 부분이 없다. 이런 부분을 충족시키기 위해서 모듈로 제공하고 있다. 

- **list가 이미 존재하는데 왜 array모듈을 사용하는 걸까?**

    list는 크기가 가변적이고 어떤 원소 타입이던 저장할 수 있다는 장점이 있지만, 메모리를 더 많이 필요로 한다는 단점이 있기 때문이다.

- **언제 사용할까?**

    동일한 유형의 많은 변수를 사용해야 하는 경우에 사용하게 된다. 또는 데이터 컬렉션을 저장하는 데에도 사용된다. 즉, 데이터를 동적으로 처리해야 하는 경우에 유용하다. 파이썬 배열은 메모리를 적게 사용하기 때문에 목록보다 훨씬 빠르다.

### [특징]

- 형은 객체 생성시에 단일 문자인 형코드를 사용하여 지정된다.
- 배열모듈을 사용해서 배열을 만드는 경우 배열의 요소는 동일한 숫자 형식이어야 한다.

![image](https://user-images.githubusercontent.com/60565941/127294274-d8f767a1-2223-41a5-86f3-ef6e492a67b8.png)

### **사용되는 함수들**

- array.**typecodes**

    배열을 만드는데 사용된 typecode문자를 반환

    ```python
    import array

    abc = array.array('d', [1,2,3])
    print(abc.typecode) # d 출력
    ```

- array.**itemsize**

    배열의 항목 길이를 반환

    ```python
    import array

    abc = array.array('d', [1,2,3])
    print(abc.itemsize) # 8 출력(d는 double형이므로 8바이트 이므로)
    ```

- array.**buffer_info**()

    배열의 내용을 담는데 사용된 버퍼의 현재 메모리주소와 요소의 수로 표현한 길이를 제공

    ```python
    import array

    abc = array.array('d', [1,2,3])
    print(abc.buffer_info()) #(24989944, 3) 
    ```

- array.**extend(iterable)**

    정확히 같은 형의 코드를 가진 배열의 끝에 추가한다(형이 다르면 TypeError발생)

    ```python
    import array

    abc = array.array('d', [1,2,3])
    tmp = array.array('d', [4,5,6])
    abc.extend(tmp)
    print(abc) # array('d', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    ```

- array.fromlist(list)

    리스트에서 항목을 추가한다

    ```python
    import array

    abc = array.array('d', [1,2,3])
    tmp = [8,9]
    abc.fromlist(tmp)
    print(abc) # array('d', [1.0, 2.0, 3.0, 4.0, 8.0, 9.0])
    ```

- array.**tolist**

    배열을 일반리스트로 변환한다

    ```python
    import array

    abc = array.array('d', [1,2,3])
    print(abc.tolist()) # [1.0, 2.0, 3.0]
    ```

## 배열 만들기

```python
import array 

abc = array.array('d',[2.5, 4.9, 6.7])
print(abc)

#결과
# array('d', [2.5, 4.9, 6.7])
```

## 배열요소에 액세스하기

```python
import array 

abc = array.array('d',[2.5, 4.9, 6.7])
print(abc[1])
print(abc[1:2]) #slice해서 접근할 수도 있다.

# 결과
# 4.9
# array('d', [4.9])
```

## 배열에 요소 삽입하기

```python
import array 

abc = array.array('i', [300,200,100])
abc.insert(2, 150) # 2번째 index에 150을 삽입한
print(abc)

#결과
# array('i', [300, 200, 150, 100])
```

## 배열에 요소 수정하기

```python
import array as myarr 
a=myarr.array('b',[3,6,4,8,10,12,14,16,18,20]) 
a[0]=99 
print(a)

import array as myarr 
first = myarr.array('b', [4, 6, 8]) 
second = myarr.array('b', [9, 12, 15]) 
numbers = myarr.array('b')   
numbers = first + second 
print(numbers)

#결과
# array('d', [2.5, 4.9, 6.7])
```

## 배열에서 요소 popup하기

```python
import array 

first = myarr.array('b', [20, 25, 30]) 
first.pop(2) 
print(first)

no = myarr.array('b', [10, 4, 5, 5, 7]) 
del no[4]  
print(no)

#결과
# array('d', [2.5, 4.9, 6.7])
```

## 배열에서 요소 삭제하기

```python
import array 

first = myarray.array('b', [2, 3, 4]) 
first.remove(3) 
print(first)
#결과
# array('d', [2.5, 4.9, 6.7])
```

## 배열에서 값의 인덱스를 검색하고 얻어보기

```python
import array 

number = myarray.array('b', [2, 3, 4, 5, 6])              
print(number.index(3))
#결과
# array('d', [2.5, 4.9, 6.7])
```

## 배열을 역순으로 바꿔보기

```python
import array 

abc = array.array('d',[2.5, 4.9, 6.7])
print(abc)

#결과
# array('d', [2.5, 4.9, 6.7])
```

## 배열을 유니코드로 변환

```python
import array 

p = array('u',[u'\u0050',u'\u0059',u'\u0054',u'\u0048',u'\u004F',u'\u004E'])
print(p)
q = p.tounicode()
print(q)
#결과
# array('d', [2.5, 4.9, 6.7])
```

## 배열에서 값 발생횟수 계산

```python
import array 

number = myarr.array('b', [2, 3, 5, 4,3,3,3]) 
print(number.count(3))
#결과
# array('d', [2.5, 4.9, 6.7])
```

## 배열을 트래버스

```python
import array 

balance = array.array('i', [300,200,100])
for x in balance:
	print(x)
#결과
# array('d', [2.5, 4.9, 6.7])
```
