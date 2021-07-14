import time
from collections import deque


def timer(f):
    start_time = time.time()
    f()
    print(f"{f.__name__}() time --- {time.time() - start_time} seconds ---")
    return f


@timer
def test_list():
    a = []
    for i in range(1000000):
        a.append(i)


@timer
def test_deque():
    a = deque()
    for i in range(1000000):
        a.append(i)


test_list()
test_deque()
