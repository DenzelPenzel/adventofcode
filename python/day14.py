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
    data = [l.strip() for l in sys.stdin]
    A = set()
    for line in data:
        pair = [list(map(int, filter(lambda xx: xx, x.split(',')))) for x in line.split('->')]
        for p1, p2 in zip(pair, pair[1:]):
            for i in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                for j in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                    A.add((j, i))

    floor = 2 + max(x[1] for x in A)
    lo_x = min(x[0] for x in A) - 2000
    hi_x = max(x[1] for x in A) + 2000

    for x in range(lo_x, hi_x):
        A.add((x, floor))

    is_over = False
    for x in range(1000000):
        start = (500, 0)
        while True:
            if start[1] + 1 >= floor and (not is_over):
                is_over = True
                print(x)  # first question
            # move down
            if (start[0], start[1] + 1) not in A:
                start = (start[0], start[1] + 1)
            elif (start[0] - 1, start[1] + 1) not in A:
                start = (start[0] - 1, start[1] + 1)
            elif (start[0] + 1, start[1] + 1) not in A:
                start = (start[0] + 1, start[1] + 1)
            else:
                break
        if start == (500, 0):
            print(x + 1)  # second question
            break
        A.add(start)
