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
schoolType = [''] + sys.stdin.readline().split()

connected_school = 1
total_weight = 0

tree_dict = {}
for i in range(1, n+1):
    if not(i in tree_dict.keys()):
        node = Tree(i)
        node.parent = node
        tree_dict[i] = node

graph = []
for _ in range(m):
    u, v, d = map(int, sys.stdin.readline().split())
    graph.append((u, v, d))

graph.sort(key=lambda x: x[2])

for u, v, d in graph:
    # 남초-남초, 여초-여초 학교끼리는 간선 X
    if schoolType[u] == schoolType[v]:
        continue

    pu = find(tree_dict[u])
    pv = find(tree_dict[v])

    if pu != pv:
        union(pu, pv)
        connected_school += 1
        total_weight += d

# 모든 학교가 연결되었는지 확인
if connected_school == n:
    sys.stdout.write(str(total_weight))
else:
    sys.stdout.write(str(-1))