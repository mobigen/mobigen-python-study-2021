# 얕은 복사와 깊은 복사 연산

Created: July 4, 2021 1:42 PM
Tags: copy, deepcopy, immutable, mutable

✔**목차**

# **복사는 언제 사용할까?**

파이썬에서는 대입문은 객체를 복사하지 않고, 대상과 **객체** 사이에 바인딩을 만든다.(객체에만 유효하다)

# **얕은 복사와 깊은 복사의 차이는 뭘까?**

- **얕은복사**

    ### copy.copy(x)

    - 새로운 복합 객체를 만들고 원본 객체를 가리키는 참조를 새로운 복합 객체에 삽입
    - **그렇기 때문에 모든 값을 독립적으로 복사할 수 없다**

- **깊은복사**

    ### copy.deepcopy(x[,memo])

    - 새로운 복합객체를 만들고, 재귀적으로 원본 객체의 사본을 새로 만든 복합 객체에 삽입

![image](https://user-images.githubusercontent.com/60565941/127294384-fcfcd462-1f05-4899-a0dc-376c5269a435.png)


![image](https://user-images.githubusercontent.com/60565941/127294411-b325540e-65b7-4f81-8438-f756a6560e6b.png)


## **mutable한 객체 변수간의 복사**

```python
a = [1,2,3]
b = a    # b에 a를 할당한다( 얕은복사 )
         # 그렇기 때문에 b는 a의 메모리 주소를 바라본다

b[0] = 5  # iterable 값을 변경

print(b)   # b = [5,2,3]
print(a)   # a = [5,2,3] 
           # b가 a를 바라보고 있기 때문에 b를 변경하면 a도 
           # 같이변경된다.
```

```python
a = [1,2,3]
b = a    # b에 a를 할당한다( 얕은복사 )
         # 그렇기 때문에 b는 a의 메모리 주소를 바라본다

a = [5,6,7]    # 값이 바뀐것으로 인식 x, 변수를 재할당 한 것

print(b)   # b = [5,2,3]
print(a)   # a = [5,2,3] 
           # b가 a를 바라보고 있기 때문에 b를 변경하면 a도 
           # 같이변경된다.
```

```python
#deepcopy
import copy

a = [1,2,3]
b = copy.deepcopy(a)

b[0] = 5

print(b) #[5,2,3]
print(a) #[1,2,3]
```

## immutable한 객체 변수간의 복사

- a변수에 첫번째 글자를 변경 시도하면 에러가 발생
- 아예 다른 값을 할당하면 id가 변경

```python
a = "abc"

print(id(a))         # 21037440
print(a[0])          # 'a'

a[0] = 'k'           # TypeError: 'str' object does not support item assignment
```

```python
a = "abc"
b = a    # b는 a의 메모리 주소를 바라본다

print(a) # 'abc' 
print(b) # 'abc'

b = "efg" # 변수가 아예 재할당 = 메모리 주소가 a와 다르다

print(id(b)) #
print(id(a)) #

```
