import sys

fibo = [[0, 0] for _ in range(41)]
fibo[0] = [1, 0]
fibo[1] = [0, 1]


def cnt_fibo(num):
    if fibo[num] != [0, 0]:
        return fibo[num]

    fibo_num = []
    if fibo[num-1] != [0, 0]:
        fibo_num = fibo[num-1]
    else:
        fibo_num = cnt_fibo(num-1)
    for i in range(2):
        fibo[num][i] += fibo_num[i]

    fibo_num = []
    if fibo[num-2] != [0, 0]:
        fibo_num = fibo[num-2]
    else:
        fibo_num = cnt_fibo(num-2)
    for i in range(2):
        fibo[num][i] += fibo_num[i]

    return fibo[num]


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(*cnt_fibo(n))
