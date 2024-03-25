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
    if a.height < b.height:
        a.parent = b
    else:
        b.parent = a

    if a.height == b.height:
        a.height += 1


n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append([c, a, b])
    graph.append([c, b, a])
graph.sort(key=lambda x: x[0])

a, b = map(int, sys.stdin.readline().split())

start, end = 1, 10**9
res = 0
while start <= end:
    mid = (start + end) // 2
    tree_dict = {}
    for i in range(1, n+1):
        node = Tree(i)
        node.parent = node
        tree_dict[i] = node

    for w, u, v in graph:
        pu = find(tree_dict[u])
        pv = find(tree_dict[v])

        if pu != pv and w >= mid:
            union(pu, pv)

    if find(tree_dict[a]) == find(tree_dict[b]):
        res = max(res, mid)
        start = mid + 1
    else:
        end = mid - 1

sys.stdout.write(str(res))
