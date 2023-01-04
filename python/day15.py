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
    def get_dist(x, y, u, z):
        return abs(x - u) + abs(y - z)


    def parse(search, start):
        x = line.find(search, start) + 2
        res = ''
        is_neg = True if line[x] == '-' else False
        if is_neg:
            x += 1
        while x < len(line) and line[x].isnumeric():
            res += line[x]
            x += 1
        return int(res) * -1 if is_neg else int(res), x


    def valid(x, y):
        for (sx, sy, d) in A:
            new_d = get_dist(x, y, sx, sy)
            if new_d <= d:
                return False
        return True


    data = [l.strip() for l in sys.stdin]
    A = set()  # sensors
    B = set()  # beacons

    for line in data:
        i, next_i = parse('x=', 0)
        j, next_j = parse('y=', 0)
        ii, _ = parse('x=', next_i)
        jj, _ = parse('y=', next_j)
        d = get_dist(i, j, ii, jj)
        A.add((i, j, d))
        B.add((ii, jj))

    res = 0
    y = int(2e6)

    for x in range(-int(1e7), int(1e7)):
        if not valid(x, y) and (x, y) not in B:
            res += 1

    print(res)

    for (x, y, d) in A:
        for dx in range(d + 2):
            dy = (d + 1) - dx
            for a, b in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
                xx = x + (dx * a)
                yy = y + (dy * b)
                if not (0 <= x <= 4000000 and 0 <= y <= 4000000):
                    continue
                assert abs(x - xx) + abs(y - yy) == d + 1
                if valid(xx, yy):
                    print(xx * 4000000 + yy)
                    exit(0)
