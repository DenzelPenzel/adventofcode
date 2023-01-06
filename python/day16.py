import collections
import heapq
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
    graph = collections.defaultdict(list)
    rates = {}

    for line in data:
        x = line.split(' ')
        rate = x[4].split('=')[1][:-1]
        rates[x[1]] = int(rate)
        if 'valves' in line:
            k = line.find('valves')
            for v in line[k + len('valves') + 1:].split(', '):
                graph[x[1]].append(v)
        elif 'valve' in line:
            k = line.find('valve')
            graph[x[1]].append(line[k + len('valve') + 1:])


    def dfs(v, times, score, visited):
        if times == 0: return 0
        key = (v, times, score)
        if key in dp:
            return dp[key]
        res = 0
        if not visited[v]:
            visited[v] = True
            res = max(res, score + dfs(v, times - 1, rates[v] + score, visited))
            visited[v] = False
        for u in graph[v]:
            res = max(res, score + dfs(u, times - 1, score, visited))
        dp[key] = res
        return res


    def bfs(graph, start, end):
        visited = set([start])
        queue = collections.deque([start])
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                v = queue.popleft()
                if v == end:
                    return steps
                for u in graph[v]:
                    if u not in visited:
                        visited.add(u)
                        queue.append(u)
            steps += 1
        return -1


    dp = {}
    visited = {x: False for x in graph.keys()}
    visited['AA'] = True

    for name in graph.keys():
        if rates[name] == 0:
            visited[name] = True

    res = dfs('AA', 30, 0, visited)
    print(res)

    # B
    room_names = ['AA']
    for x in graph:
        if rates[x] != 0:
            room_names.append(x)

    room_names.sort()
    flow_rates = {}

    for i, name in enumerate(room_names):
        flow_rates[i] = rates[name]

    len_rooms = len(room_names)
    weight_graph = [[0] * len_rooms for _ in range(len_rooms)]
    max_visited_state = collections.defaultdict(int)

    # calculate undirected weighted graph for the all paths
    for i, start in enumerate(room_names):
        for j, end in enumerate(room_names):
            if start == end:
                continue
            steps = bfs(graph, start, end)
            weight_graph[i][j] = steps
            weight_graph[j][i] = steps

    # get max sum for all possible states
    def dfs_high_pressure(time, flow_rate, v, total_pressure, visited):
        if time < 0:
            return

        if time == 0:
            key = ''.join(visited)
            max_visited_state[key] = max(max_visited_state[key], total_pressure)
            return

        dfs_high_pressure(0, flow_rate, v, total_pressure + flow_rate * time, visited)

        for u in range(len_rooms):
            if visited[u] == '1':
                continue

            reach_time = weight_graph[v][u] + 1

            if time < reach_time:
                continue

            visited[u] = '1'
            dfs_high_pressure(time - reach_time, flow_rate + flow_rates[u], u,
                              total_pressure + flow_rate * reach_time, visited)
            visited[u] = '0'


    dfs_high_pressure(26, 0, 0, 0, ['0'] * len_rooms)
    all_states = []
    res = 0

    for state, value in max_visited_state.items():
        mask = 0
        for i, v in enumerate(state):
            if v == '1':
                mask |= (1 << i)
        all_states.append({'mask': mask, 'value': value})

    all_states.sort(key=lambda x: x['value'], reverse=True)

    for p1 in all_states:
        for p2 in all_states:
            total_sum = p1['value'] + p2['value']
            if res > total_sum:
                break
            if p1['mask'] & p2['mask'] == 0:
                res = max(res, total_sum)

    print(res)
