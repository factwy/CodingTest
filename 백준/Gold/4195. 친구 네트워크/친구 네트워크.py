import sys


class Tree:
    def __init__(self, name, parent, height=1, friend=1):
        self.name = name
        self.parent = parent
        self.height = height
        self.friend = friend


def find(p):
    if p.name == p.parent.name:
        return p
    p.parent = find(p.parent)
    return p.parent


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

        pa.friend += pb.friend
        pb.friend = pa.friend

    sys.stdout.write(str(pa.friend) + "\n")


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    f = int(sys.stdin.readline().rstrip())
    people = {}

    for _ in range(f):
        name = sys.stdin.readline().rstrip().split()
        for n in name:
            if not (n in people.keys()):
                tree = Tree(n, None)
                tree.parent = tree
                people[n] = tree

        union(people[name[0]], people[name[1]])