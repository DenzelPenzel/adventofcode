import collections
import itertools
import math
import os
import sys
from functools import reduce
from itertools import zip_longest
from typing import Iterable


def read_file(fname: str):
    with open(fname, mode='r') as f:
        content = f.readlines()
        context = [list(map(int, x.strip().split(' '))) for x in content]
    return context


if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


# array
def mp(): return map(int, sys.stdin.readline().split())


# string
def st(): return list(sys.stdin.readline().strip())


if __name__ == '__main__':
    data = list(filter(lambda x: x, [l.strip() for l in sys.stdin]))


    def grouper(n, iterable, fillvalue=None):
        "Collect data into fixed-length chunks or blocks"
        # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return zip_longest(fillvalue=fillvalue, *args)


    def is_same(x, y):
        if isinstance(x, int) and isinstance(y, int):
            if x == y:
                return 0
            if x > y:
                return -1
            return 1
        elif isinstance(x, list) and isinstance(y, list):
            i = 0
            while i < len(x) and i < len(y):
                res = is_same(x[i], y[i])
                if res == 1:
                    return 1
                if res == -1:
                    return -1
                i += 1
            if i == len(x) and i < len(y):
                return 1
            if i < len(x) and i == len(y):
                return -1
            return 0
        elif isinstance(x, int) and isinstance(y, list):
            return is_same([x], y)
        else:
            return is_same(x, [y])


    res = 0
    idx = 1
    packets = []
    for x, y in grouper(2, data):
        xx = eval(x)
        yy = eval(y)
        packets.append(xx)
        packets.append(yy)
        if is_same(xx, yy) == 1:
            res += idx
        idx += 1
    print(res)

    packets.append([2])
    packets.append([6])

    ids = []
    from functools import cmp_to_key

    packets = sorted(packets, key=cmp_to_key(lambda p1, p2: is_same(p1, p2)), reverse=True)

    for i, v in enumerate(packets):
        if v == [2] or v == [6]:
            ids.append(i + 1)

    print(math.prod(ids))
