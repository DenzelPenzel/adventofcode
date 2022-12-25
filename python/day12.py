import collections
import math
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
    def fn(queue, target):
        dist = [[float('inf')] * m for _ in range(n)]
        for i, j in queue:
            dist[i][j] = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                if (i, j) == target:
                    return dist[target[0]][target[1]]
                for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if 0 <= x < n and 0 <= y < m:
                        if dist[x][y] > dist[i][j] + 1 and A[x][y] - A[i][j] <= 1:
                            dist[x][y] = dist[i][j] + 1
                            queue.append((x, y))
        return -1


    data = [l.strip() for l in sys.stdin]
    n, m = len(data), len(data[0])
    A = [[None] * m for _ in range(n)]
    queue = collections.deque()
    target = None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                A[i][j] = 0
                queue.append((i, j))
            elif data[i][j] == 'E':
                A[i][j] = 25
                target = (i, j)
            else:
                A[i][j] = ord(data[i][j]) - 97
                if A[i][j] == 0:
                    queue.append((i, j))

    print(fn(queue, target))
