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
graph = []
tree_dict = {}

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())

    if not(x in tree_dict.keys()):
        node = Tree(x)
        node.parent = node
        tree_dict[x] = node
    if not(y in tree_dict.keys()):
        node = Tree(y)
        node.parent = node
        tree_dict[y] = node

    graph.append((x, y, z))

graph.sort(key=lambda x: x[2])

total_weight, last_weight = 0, 0

for x, y, z in graph:
    px = find(tree_dict[x])
    py = find(tree_dict[y])

    if px != py:
        union(px, py)
        total_weight += z
        last_weight = z

res = total_weight - last_weight
sys.stdout.write(str(res))