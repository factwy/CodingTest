import sys


class Tree:
    def __init__(self, val, parent, height=1):
        self.val = val
        self.parent = parent
        self.height = height


def find(node):
    if node.val == node.parent.val:
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


def kruskal(graph):
    mst = 0

    for a, b, c in graph:
        pa = find(a)
        pb = find(b)

        if pa == pb:
            continue

        union(pa, pb)
        mst += c

    return mst


v, e = map(int, sys.stdin.readline().strip().split())
treedict = {}
graph = []

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split())

    if not (a in treedict.keys()):
        node = Tree(a, None)
        node.parent = node
        treedict[a] = node
    if not (b in treedict.keys()):
        node = Tree(b, None)
        node.parent = node
        treedict[b] = node

    graph.append((treedict[a], treedict[b], c))

graph.sort(key=lambda x: x[2])

sys.stdout.write(str(kruskal(graph)))
