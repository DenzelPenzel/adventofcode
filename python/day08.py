import collections
import heapq
import os
import sys
from itertools import product
from functools import reduce
from typing import List


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
    n, m = len(data), len(data[0])
    A = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            A[i][j] = int(data[i][j])

    dp = [[False] * m for _ in range(n)]
    res = 0

    for i in range(n):
        height = -1
        for j in range(m):
            if A[i][j] > height:
                height = A[i][j]
                dp[i][j] = True

        height = -1
        for j in range(m - 1, -1, -1):
            if A[i][j] > height:
                height = A[i][j]
                dp[i][j] = True

    for j in range(m):
        height = -1
        for i in range(n):
            if A[i][j] > height:
                height = A[i][j]
                dp[i][j] = True

        height = -1
        for i in range(n - 1, -1, -1):
            if A[i][j] > height:
                height = A[i][j]
                dp[i][j] = True

    for i in range(n):
        for j in range(m):
            if dp[i][j]:
                res += 1

    print(res)

    # B
    res = 0

    for i in range(n):
        for j in range(m):
            c = []
            k = j + 1
            cnt = 0
            while k < m and A[i][j] > A[i][k]:
                k += 1
                cnt += 1
            c.append(cnt + 1 if k < m else cnt)
            k = j - 1
            cnt = 0
            while k >= 0 and A[i][j] > A[i][k]:
                k -= 1
                cnt += 1
            c.append(cnt + 1 if k >= 0 else cnt)
            cnt = 0
            k = i + 1
            while k < n and A[i][j] > A[k][j]:
                k += 1
                cnt += 1
            c.append(cnt + 1 if k < n else cnt)
            cnt = 0
            k = i - 1
            while k >= 0 and A[i][j] > A[k][j]:
                k -= 1
                cnt += 1
            c.append(cnt + 1 if k >= 0 else cnt)
            res = max(res, reduce(lambda a, b: a * b, c, 1))

    print(res)
