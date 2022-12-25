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
    def fn(idx, x):
        global res
        idx1 = idx - 1
        dp[idx1 // 40][idx1 % 40] = ('#' if abs(x - (idx1 % 40)) <= 1 else ' ')
        if idx in [20, 60, 100, 140, 180, 220]:
            res += x * idx


    data = [l.strip() for l in sys.stdin]
    dp = [['?' for _ in range(40)] for _ in range(6)]

    x = 1
    idx = 0
    res = 0
    for line in data:
        p = line.split(' ')
        if p[0] == 'noop':
            idx += 1
            fn(idx, x)
        else:
            idx += 1
            fn(idx, x)
            idx += 1
            fn(idx, x)
            x += int(p[1])
    print(res)

    for x in range(6):
        print(''.join(dp[x]))
