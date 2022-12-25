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
    def get_dist(x, y, u, z):
        return abs(x - u) + abs(y - z)

    def get_diag_dist(x, y, u, z):
        return max(abs(x - u), abs(y - z))

    def get_next_pos(start, end):
        d = [get_dist(*start, *end), get_diag_dist(*start, *end)]
        if min(d) <= 1: return start
        i, j = start
        coords = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)] if d[0] <= d[1] else [(i + 1, j + 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1)]
        c = []
        for x, y in coords:
            c.append(([x, y], get_dist(*[x, y], *end)))
        return sorted(c, key=lambda x: x[1])[0][0]

    data = [l.strip() for l in sys.stdin]
    seen = set([(0, 0)])
    n = 9
    positions = [[0, 0] for _ in range(n)]

    for x in data:
        dir, steps = x.split(' ')
        for _ in range(int(steps)):
            if dir == 'R': positions[0][1] += 1
            if dir == 'L': positions[0][1] -= 1
            if dir == 'U': positions[0][0] -= 1
            if dir == 'D': positions[0][0] += 1
            for k in range(1, len(positions)):
                positions[k] = get_next_pos(positions[k], positions[k - 1])
            seen.add(tuple(positions[-1]))
    res = len(seen)
    print(res)
