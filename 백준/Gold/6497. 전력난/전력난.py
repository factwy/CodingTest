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


m, n = map(int, sys.stdin.readline().split())
while m != 0 and n!= 0:
    tree_dict = {}
    graph = []

    total_dis, min_dis = 0, 0

    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        total_dis += z

        if not(x in tree_dict.keys()):
            node = Tree(x)
            node.parent = node
            tree_dict[x] = node
        if not(y in tree_dict.keys()):
            node = Tree(y)
            node.parent = node
            tree_dict[y] = node

        graph.append((tree_dict[x], tree_dict[y], z))

    graph.sort(key=lambda x:x[2])

    for x, y, z in graph:
        px = find(x)
        py = find(y)

        if px != py:
            union(px, py)
            min_dis += z

    sys.stdout.write(str(total_dis - min_dis) + "\n")
    m, n = map(int, sys.stdin.readline().split())