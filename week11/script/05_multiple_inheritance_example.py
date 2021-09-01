class A(object):
    def __init__(self):
        print('A class')


class B(A):
    def __init__(self):
        print('B class')
        super().__init__()


class C(A):
    def __init__(self):
        print('C class')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('D class')
        super().__init__()


d = D()
