a = type('MyClass', (object,), {'a': 3, 'm': lambda x, y: x + y})  # type(클래스명, 상속클래스, 속성/메소드)
print(a)
print(a.a)
print(a.m(3, 4))


class MyMetaClass(type):
    def __new__(mcs, cls_name, bases, namespace):
        assert type(namespace['a']) is int, 'the a is not integer'
        return type.__new__(mcs, cls_name, bases, namespace)


class MyClass(metaclass=MyMetaClass):
    a = 3.14


a = MyClass()
