import sys


class Tree:
    def __init__(self, val, price, parent=None):
        self.val = val
        self.price = price
        self.parent = parent


def find(node):
    if node == node.parent:
        return node
    node.parent = find(node.parent)
    return node.parent


def union(a, b):
    b.parent = a
    a.price = min(a.price, b.price)


n, m, k = map(int, sys.stdin.readline().split())
friend_price =  list(map(int, sys.stdin.readline().split()))

tree_dict = {}
for i in range(1, n+1):
    node = Tree(i, friend_price[i-1])
    node.parent = node
    tree_dict[i] = node

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    pa = find(tree_dict[a])
    pb = find(tree_dict[b])

    if pa != pb:
        union(pa, pb)

parents = set()
for t in tree_dict.values():
    parents.add(find(t))

total_min_price = 0
for p in parents:
    total_min_price += p.price

if total_min_price > k:
    sys.stdout.write("Oh no")
else:
    sys.stdout.write(str(total_min_price))