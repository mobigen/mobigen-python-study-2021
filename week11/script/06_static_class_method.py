class A(object):
    cnt = 0

    def instance_method(self, b: int):
        self.cnt += b


print("A Class")
a = A()
print(f"A class's cnt: [{A.cnt}], a instance's cnt : [{a.cnt}]")
a.instance_method(3)
print(f"A class's cnt: [{A.cnt}], a instance's cnt : [{a.cnt}]")


class B(object):
    cnt = 0

    @classmethod
    def class_method(cls, b: int):
        cls.cnt += b


print("\nB Class")
b = B()
print(f"B class's cnt: [{B.cnt}], b instance's cnt : [{b.cnt}]")
B.class_method(3)
print(f"B class's cnt: [{B.cnt}], b instance's cnt : [{b.cnt}]")


class C(object):
    cnt = 0

    @staticmethod
    def static_method(x: int, y: int):
        return x + y


print("\nC Class")
print(C.static_method(1, 3))
