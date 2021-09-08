import time

from collections import defaultdict


def counter(f):
    def _():
        cnt = 0
        group = defaultdict(int)
        for i in f():
            group[i['group']] += 1
            cnt += 1
        return group, cnt
    return _


def timer(f):
    def _():
        st = time.time()
        result = f()
        return result, time.time() - st
    return _
