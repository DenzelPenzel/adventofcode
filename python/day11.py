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
    data = [l.strip() for l in sys.stdin]
    mapping = {}
    current_id = None
    dividers = []
    for line in data:
        if line.count("Monkey"):
            x = line.split(' ')
            k = x[1].find(':')
            current_id = x[1][:k]
            mapping[current_id] = {}
        if line.count("Starting"):
            k = line.find("items:")
            x = list(map(int, line[k + len("items:") + 1:].split(", ")))
            mapping[current_id]["items"] = collections.deque(x)
        elif line.count("Operation"):
            k = line.find("=")
            mapping[current_id]["ops"] = line[k + 2:].split(" ")
        elif line.count("Test"):
            x = line.split(" ")
            mapping[current_id]["divisible"] = int(x[-1])
            dividers.append(int(x[-1]))
        elif line.count("true"):
            x = line.split(" ")
            mapping[current_id]["true"] = x[-1]
        elif line.count("false"):
            x = line.split(" ")
            mapping[current_id]["false"] = x[-1]
    monkey_counter = collections.Counter()
    div_prod = math.prod(dividers)
    for _ in range(10000):
        for idx in mapping.keys():
            monkey_counter[idx] += len(mapping[idx]['items'])
            while mapping[idx]['items']:
                x = mapping[idx]['items'].popleft()
                ops = mapping[idx]['ops']
                divisor = mapping[idx]['divisible']
                a = x if ops[0] == 'old' else int(ops[0])
                b = x if ops[2] == 'old' else int(ops[2])
                if ops[1] == '+':
                    xx = a + b
                if ops[1] == '*':
                    xx = a * b
                xx %= div_prod
                if xx % mapping[idx]['divisible'] == 0:
                    next_id = mapping[idx].get('true')
                    mapping[next_id]['items'].append(xx)
                else:
                    next_id = mapping[idx].get('false')
                    mapping[next_id]['items'].append(xx)
    res = math.prod([x[1] for x in monkey_counter.most_common(2)])
    print(res)
