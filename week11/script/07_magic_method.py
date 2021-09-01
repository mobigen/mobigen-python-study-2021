class NewInt(object):
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


new_int_a = NewInt(3)
new_int_b = NewInt(4)
print(f"더하기 결과 : {new_int_a + new_int_b}")
# print(f"빼기 결과 : {new_int_a - new_int_b}")  # 빼기는 구현하지 않아서 오류 발생


# example 2 ===================================


class A(object):
    pass


class B(object):
    def __enter__(self):
        print("__enter__ is called")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ is called")
        pass


# with A() as a:
#     print(a)


with B() as b:
    print(b)
