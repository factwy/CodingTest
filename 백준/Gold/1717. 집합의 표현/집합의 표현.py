import sys

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
node_rank = [0 for i in range(n+1)]


def find(idx):
    if idx == parent[idx]:
        return idx
    parent[idx] = find(parent[idx])
    return parent[idx]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        if node_rank[a] < node_rank[b]:
            parent[pa] = pb
        else:
            parent[pb] = pa

        if node_rank[pa] == node_rank[pb]:
            node_rank[pb] += 1


for _ in range(m):
    check, a, b = map(int, sys.stdin.readline().split())

    if check == 0:
        # 합집합
        union(a, b)
    else:
        # 집합 확인
        pa = find(a)
        pb = find(b)

        if pa != pb:
            sys.stdout.write("NO\n")
        else:
            sys.stdout.write("YES\n")