# 약한 참조

Created: July 4, 2021 1:37 PM
Tags: GC, GarbageCollection, referenceCounting, weakref

✔**목차**

---

약한참조를 알아보기 전에 Garbage Collection(GC)에 대해 공부하면 좋을것 같습니다!
+ 약한 참조를 사용하는 방법보다는, 원리를 이해하여 코딩할 때 메모리 누수를 최적화시킬 수 있는 방법에 대해 깊은 고민을 하는 것이 좋을것 같습니다!

# **파이썬에서의 GC**

파이썬은 내부적으로 malloc() 과 free()를 많이 사용하기 때문에 메모리 누수 위험이 있다. 이를 위해 메모리를 관리하기 위해 아래 두가지 방법을 사용한다.

- **Generational Garbage Collection**
    - 순환참조에 주로 사용(참조추가를 감지하여 메모리 누수를 방지)
    - Generational Hypothesis라는 가설(대부분의 객체는 생성되고 곧 버려지게 된다, 젊은 객체가 오래된 객체를 참조하는 상황은 드물다)을 기반으로 작동
    - 그렇기 때문에 대부분이 젊은 객체가 존재하며, GC가 젊은 객체를 위주로 관리해준다.
- **Reference Counting** → 주로 사용
    - 파이썬에서는 2. Reference Counting을 주로 사용
    - 객체를 만들때마다 그 객체가 사용되고 있는지를 카운팅
    - 객체가 참조되는 증가, 참조가 해제되면 감소
    - 카운팅이 0이 되면 메모리를 반환

# **약한참조가 쓰이는 이유?**

클래스 인스턴스의 속성이 만약 다른 클래스의 인스턴스를 참조하거나, 동일 클래스의 다른 인스턴스를 참조할 가능성이 높다면 메모리 누수가 발생할 가능성이 높아진다.

→ 그래서 파이썬에서는 이런 문제를 간단히 처리하기 위해서 약한 참조를 제공하고 있다. 

# **약한참조란?**

말그대로 대상객체를 참조는 하지만, 대상 객체에 대한 소유권을 주장하지는 않는 참조를 의미한다. 즉, reference count를 올리지 않는 참조를 말한다.

- 참조하려는 대상이 파괴되었다면 약한 참조는 참조대상에 대한 액세스를 요청받을 때 None을 리턴한다

# **어떻게 사용하면 될까?**

weakref 모듈의 ref라는 클래스를 통해서 생성할 수 있다.

**[주로 사용하는 함수]**

- **weakref.ref(object[, callback])**

     :객체에 대한 약한 참조 객체를 반환

    - 객체가 메모리에 존재하면 객체에 대한 참조를 반환.
    - 그렇지 않으면 None을 반환
- **weakref.proxy(object[, callback])**

    : 객체에 대한 약한 참조 프록시를 생성

    - 명시적으로 약한 참조 객체를 생성하는 대신, 프록시를 이용하여 객체 참조를 얻을 수 있음
- **weakref.getweakrefcount(object)**

    : 객체에 대한 약한 참조 카운터를 반환

- **weakref.getweakrefs(object)**

    : 객체를 참조하는 약한 참조 객체와 프록시를 리스트로 반환

- **weakref.WeakKeyDictionary([dict])**

    : 키를 약하게 참조하는 매핑 클래스

    - 키에 대한 강한 참조가 더이상 없으면 딕셔너리의 항목이 삭제됨
- **weakref.WeakValueDictionary([dict])**

    : 값을 약하게 참조하는 매핑 클래스

    - 값에 대한 강한 참조가 더이상 없으면 딕셔너리의 항목이 삭제됨

**[예제]**

**변수에 값을 그냥 대입                                                 vs                                                         weakref모듈로 약한참조 이용**

참조값은 늘어나지 않고, 값만 들어간것을 볼 수 있다.

```python
###변수에 값을 그냥 대입하는 경우
import sys
# 1. 현재 노트북에서 참조값
print(sys.getrefcount(1))        # 94
va = 1

# 2. 그냥 변수에 값을 대입했을때 참조값이 95로 늘어난다
print(sys.getrefcount(1))        # 95
del va

# 3. 변수를 지우면 다시 원래 참조값으로 돌아온다
print(sys.getrefcount(1))        # 94
```

```python
### weakref 모듈을 이용해, 약한참조를 이용하는 경우
import weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                            # 참조를 생성한다
d = weakref.WearkRefDictionary()
d['primary'] = a                    # 참조는 생성하지 않는다
d['primary']                        # 10 (값이 있는 경우만 출려됨)
del a                                # 참조를 삭제한다
gc.collect()                        # 0 (가비지콜렉션을 바로 실행한다)
d['primary']                        # 자동으로 삭제됨
```

# **약한 참조를 써야할 곳은 어디일까?**

- 한개 이상의 객체가 참조 순환 고리를 만드는 경우에 메모리 누수를 방지하기 위해서 사용한다.
- 큰 객체를 보유하고 있는 매핑에도 사용된다고 한다. (큰 바이너리 이미지 객체와 이름을 딕셔너리를 이용하여 매핑할 때)
- 큰 객체를 보유하고 있는 캐싱에도 사용된다고 한다.
