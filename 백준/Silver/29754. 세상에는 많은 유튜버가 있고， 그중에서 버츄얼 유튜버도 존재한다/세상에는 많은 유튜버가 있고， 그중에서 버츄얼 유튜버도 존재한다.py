import sys


def count(s, e):
    s_h, s_m = map(int, s.split(":"))
    e_h, e_m = map(int, e.split(":"))

    dist_m = e_m - s_m
    dist_h = e_h - s_h
    dist = dist_h * 60 + dist_m

    return dist


n, m = map(int, sys.stdin.readline().split())
week = (m+6) // 7
need_broadcast = 60 * 60
need_broadcast_trial = 5
broadcast = {}

for _ in range(n):
    input_data = sys.stdin.readline().split()
    name = input_data[0]
    day = int(input_data[1])
    s = input_data[2]
    e = input_data[3]

    if name not in broadcast.keys():
        broadcast[name] = [[0, 0] for _ in range(week)]    # trial, time

    broadcast[name][(day-1)//7][0] += 1
    broadcast[name][(day-1)//7][1] += count(s, e)

res = []
for name in broadcast.keys():
    check = True

    for w in range(week):
        if broadcast[name][w][0] < need_broadcast_trial:
            check = False
            break
        if broadcast[name][w][1] < need_broadcast:
            check = False
            break

    if check:
        res.append(name)

res.sort()

if res:
    for name in res:
        print(name)
else:
    print("-1")
