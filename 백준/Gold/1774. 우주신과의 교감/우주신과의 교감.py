import sys


class Tree:
    def __init__(self, val, parent=None, height=1):
        self.val = val
        self.parent = parent
        self.height = height


def find(node):
    if node == node.parent:
        return node
    node.parent = find(node.parent)
    return node.parent


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        if pa.height < pb.height:
            pa.parent = pb
        else:
            pb.parent = pa

        if pa.height == pb.height:
            pa.height += 1


n, m = map(int, sys.stdin.readline().split())
spaceship = [()]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    spaceship.append((x, y))

tree_dict = {}
graph = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        x1, y1 = spaceship[i]
        x2, y2 = spaceship[j]

        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        if not(i in tree_dict.keys()):
            node = Tree(i)
            node.parent = node
            tree_dict[i] = node
        if not(j in tree_dict.keys()):
            node = Tree(j)
            node.parent = node
            tree_dict[j] = node

        graph.append((tree_dict[i], tree_dict[j], dist))

graph.sort(key=lambda x: x[2])

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    pi = find(tree_dict[i])
    pj = find(tree_dict[j])

    union(pi, pj)


total_weight = 0.0
for u, v, w in graph:
    pu = find(u)
    pv = find(v)

    if pu != pv:
        union(pu, pv)
        total_weight += w

sys.stdout.write("{:.2f}".format(total_weight))