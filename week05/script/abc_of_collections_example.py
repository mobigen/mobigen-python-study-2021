from collections.abc import Sequence


class A(Sequence):
    pass


# a = A()  # TypeError: Can't instantiate abstract class A with abstract methods __getitem__, __len__


class B(Sequence):
    def __getitem__(self, item):
        print('getitem')
        return 1

    def __len__(self):
        print('length')
        return 0


b = B()
print(b[0])  # getitem
print(len(b))  # length
