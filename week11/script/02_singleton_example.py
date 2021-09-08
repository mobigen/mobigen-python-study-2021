# class SingletonMeta(type):
#     _instance = None
#
#     def __call__(cls, *args, **kwargs):
#         if cls._instance is None:
#             print('creating the new instance')
#             cls._instance = super().__call__(*args, **kwargs)
#         return cls._instance

class SingletonClass(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('__new__ is first called')
            cls._instance = super().__new__(cls)
        else:
            print('__new__ is second called')
        return cls._instance

    def __init__(self, alpha: int):
        self.alpha = alpha


print('== start ==')
a = SingletonClass(1)
print(a, a.alpha)
b = SingletonClass(2)
print(b, b.alpha)
print(a, a.alpha)
