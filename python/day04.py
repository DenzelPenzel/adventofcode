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
    def overlap(A, B):
        return B[1] >= A[0] and A[1] >= B[0]


    data = [l.strip() for l in sys.stdin]
    res1 = 0
    res2 = 0
    for x in data:
        [a, b] = x.split(',')
        A = list(map(int, a.split('-')))
        B = list(map(int, b.split('-')))

        if B[0] <= A[0] and B[1] >= A[1] or B[0] >= A[0] and A[1] >= B[1]:
            res1 += 1

        if overlap(A, B) or overlap(B, A):
            res2 += 1

    print(res1)
    print(res2)
