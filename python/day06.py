import collections
import heapq
import os
import sys


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
    s = sys.stdin.readline().strip()
    start, end = 0, 0
    seen = set()
    while end < len(s) and len(seen) < 14:
        while s[end] in seen and start < end:
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        end += 1

    print(end)


