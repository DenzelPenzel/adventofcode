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
    data = [l.strip() for l in sys.stdin]
    st = []
    for i, x in enumerate(data):
        try:
            int(x[0])
            size = len(x.split('   '))
            st = [[] * size for _ in range(size)]
            break
        except Exception as ex:
            pass

    for k in range(i - 1, -1, -1):
        row = data[k]
        j, idx = 0, 0
        while j < len(row):
            if row[j] == '[':
                st[idx].append(row[j + 1])
            idx += 1
            j += 4

    for k in range(i + 2, len(data)):
        actions = data[k].split(' ')
        steps, start, end = list(map(int, [actions[1], actions[3], actions[5]]))
        crates = [st[start - 1].pop() for _ in range(steps)][::-1]
        for x in crates: st[end - 1].append(x)

    print(*[st[i][-1] for i in range(len(st))])
