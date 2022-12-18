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


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.children = []
        self.parent = None
        self.size = 0


if __name__ == '__main__':
    data = [l.strip() for l in sys.stdin]
    mapping = {}
    root = Node("/")
    node = root

    for d in data:
        shell = d.split(' ')

        if shell[0] == '$':
            if shell[1] == 'cd':
                target = shell[2]
                if target == '..':
                    node = node.parent
                else:
                    new_dir = Node(shell[2])
                    new_dir.parent = node
                    node.children.append(new_dir)
                    node = new_dir
        else:
            if shell[0] == 'dir':
                pass
            else:
                size = int(shell[0])
                dummy = node
                while dummy:
                    dummy.size += size
                    dummy = dummy.parent

    def dfs(node: Node):
        global total
        if node.size <= 100000:
            total += node.size
        for next_node in node.children:
            dfs(next_node)

    def dfs2(node: Node, root_size: int):
        global best_chose
        if root_size - node.size <= 70000000-30000000:
            if best_chose is None or node.size < best_chose:
                best_chose = node.size
        for next_node in node.children:
            dfs2(next_node, root_size)

    root: Node = root.children[0]
    total = 0
    dfs(root)
    print(total)
    best_chose = None
    dfs2(root, root.size)
    print(best_chose)