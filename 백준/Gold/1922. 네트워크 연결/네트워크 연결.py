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
    pa = a.parent
    pb = b.parent

    if pa != pb:
        if pa.height < pb.height:
            pa.parent = pb
        else:
            pb.parent = pa

        if pa.height == pb.height:
            pa.height += 1


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
treedict = {}
graph = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if not(a in treedict.keys()):
        node = Tree(a)
        node.parent = node
        treedict[a] = node
    if not(b in treedict.keys()):
        node = Tree(b)
        node.parent = node
        treedict[b] = node

    graph.append((a, b, c))

graph.sort(key=lambda x: x[2])
dist = 0

for a, b, c in graph:
    pa = find(treedict[a])
    pb = find(treedict[b])

    if pa != pb:
        union(treedict[a], treedict[b])
        dist += c

sys.stdout.write(str(dist))