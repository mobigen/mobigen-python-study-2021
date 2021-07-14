import time
from collections import deque


def timer(f):
    def _():
        start_time = time.time()
        f()
        print(f"{f.__name__}() time --- {time.time() - start_time} seconds ---")
    return _


@timer
def test_list_append():
    a = []
    for i in range(1000000):
        a.append(i)


@timer
def test_deque_append():
    a = deque()
    for i in range(1000000):
        a.append(i)


@timer
def test_list_insert():
    a = []
    for i in range(100000):
        a.insert(0, i)


@timer
def test_deque_insert():
    a = deque()
    for i in range(100000):
        a.insert(0, i)


test_list_append()
test_deque_append()
test_list_insert()
test_deque_insert()
