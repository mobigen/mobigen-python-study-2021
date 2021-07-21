# abc 사용 예제

from abc import ABC, abstractmethod


class ClassA(ABC):
    @abstractmethod
    def method_a(self):
        pass


class ClassB(ClassA):
    pass


class ClassC(ClassA):
    def method_a(self):
        print("ClassC - method_a")


# b = ClassB()  # TypeError: Can't instantiate abstract class B with abstract methods method_a

# success
c = ClassC()
c.method_a()


# ======================================
# python 2 버전에서 추상 클래스 구현 예제


class ClassAA():
    def method_aa(self):
        raise NotImplementedError


class ClassBB(ClassAA):
    pass


bb = ClassBB()
bb.method_aa()  # NotImplementedError raised
