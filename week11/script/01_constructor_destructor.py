class MyClass(object):
    def __new__(cls, *args, **kwargs):
        print('__new__ is called')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print('__init__ is called')
        self.alpha = 1

    def __del__(self):
        print('__del__ is called')


print('== start ==')
print(MyClass, type(MyClass))
mc = MyClass()
print(mc, type(mc))
del mc
