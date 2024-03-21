import sys

n, m, k = map(int, sys.stdin.readline().split())
pos = list(map(int, sys.stdin.readline().split()))

start, end = 1, n
res = ""
while start <= end:
    mid = (start + end) // 2
    check = False

    for i in range(k):
        l, people = i, 1
        my_pos = '0' * i + '1'
        for j in range(i+1, k):
            if pos[j] - pos[l] >= mid:
                people += 1
                l = j
                my_pos += '1'
            else:
                my_pos += '0'

            if people == m:
                for _ in range(j+1, k):
                    my_pos += '0'
                break

        if people == m:
            res = my_pos
            check = True
            break

    if check:
        start = mid + 1
    else:
        end = mid - 1

sys.stdout.write(res)
