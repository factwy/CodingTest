import sys


class Tree:
    def __init__(self, val ,parent=None, height=1):
        self.val = val
        self.parent = parent
        self.height = height


def find(node):
    if node == node.parent:
        return node
    node.parent = find(node.parent)
    return node.parent


def union(a, b):
    if a.height < b.height:
        a.parent = b
    else:
        b.parent = a

    if a.height == b.height:
        a.height += 1


def kruskal(graph):
    k = 0
    for w, u, v in graph:
        pu = find(u)
        pv = find(v)

        if pu != pv:
            union(pu, pv)
            k += w
    return k


n, m = map(int, sys.stdin.readline().split())
min_dict, min_graph = {}, []
max_dict, max_graph = {}, []

for _ in range(m+1):
    a, b, c = map(int, sys.stdin.readline().split())

    # 오르막길과 내리막길 가중치 변환
    if c == 0:
        c = 1
    else:
        c = 0

    if not(a in min_dict.keys()):
        node = Tree(a)
        node.parent = node
        min_dict[a] = node
    if not(b in min_dict.keys()):
        node = Tree(b)
        node.parent = node
        min_dict[b] = node
    if not(a in max_dict.keys()):
        node = Tree(a)
        node.parent = node
        max_dict[a] = node
    if not(b in max_dict.keys()):
        node = Tree(b)
        node.parent = node
        max_dict[b] = node

    min_graph.append((c, min_dict[a], min_dict[b]))
    max_graph.append((-c, max_dict[a], max_dict[b]))
    # min_graph : 내리막길 우선
    # max_graph : 오르막길 우선

min_graph.sort(key=lambda x: x[0])
max_graph.sort(key=lambda x: x[0])

min_k = kruskal(min_graph)
max_k = kruskal(max_graph)

sys.stdout.write(str(max_k ** 2 - min_k ** 2))