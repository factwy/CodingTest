import sys

t = int(sys.stdin.readline().rstrip())
for num in range(1, t+1):
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    row = [[] for _ in range(9)]
    col = [[] for _ in range(9)]
    squ = [[] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            row[i].append(arr[i][j])
            col[j].append(arr[i][j])
            squ[(i//3)*3 + (j//3)].append(arr[i][j])

    check = False
    for i in range(9):
        if len(set(row[i])) != 9:
            check = True
            break
        if len(set(col[i])) != 9:
            check = True
            break
        if len(set(squ[i])) != 9:
            check = True
            break

    res = f"Case {num}: "
    if check:
        res += "INCORRECT\n"
    else:
        res += "CORRECT\n"

    sys.stdout.write(res)
    _ = sys.stdin.readline()
    