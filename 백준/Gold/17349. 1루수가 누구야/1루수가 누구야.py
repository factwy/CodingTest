import sys

command = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
target = -1

for liar in range(1, 10):
    player = [0] * 10   # 0 : 정보 없음, 1 : 1루수 X, 2 : 1루수 O
    check1 = True

    for index, (isOk, people) in enumerate(command):
        if index+1 == liar:
            if isOk == 1:
                if player[people] == 2:
                    check1 = False
                    break
                player[people] = 1
            else:
                if player[people] == 1:
                    check1 = False
                    break
                player[people] = 2
        else:
            if isOk == 1:
                if player[people] == 1:
                    check1 = False
                    break
                player[people] = 2
            else:
                if player[people] == 2:
                    check1 = False
                    break
                player[people] = 1

    if not check1:
        continue

    pl_dict = {0: 0, 1: 0, 2: 0}
    pos0, pos2 = 0, 0
    for i in range(1, 10):
        pl_dict[player[i]] += 1
        if player[i] == 0:
            pos0 = i
        elif player[i] == 2:
            pos2 = i

    if pl_dict[2] == 0 and pl_dict[0] > 1:
        target = -1
        break

    if pl_dict[2] == 1:
        if target == pos2:
            continue
        if target != -1:
            target = -1
            break
        target = pos2
    elif pl_dict[2] == 0 and pl_dict[0] == 1:
        if target == pos0:
            continue
        if target != -1:
            target = -1
            break
        target = pos0

sys.stdout.write(str(target))
