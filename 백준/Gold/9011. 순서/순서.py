import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))

    result = [0] * n
    numbers = []
    check = True

    for i in range(n-1, -1, -1):
        num = arr[i] + 1  # cur

        size = 0  # cnt
        for number in numbers:
            if num+size >= number:
                size += 1
            else:
                break

        # print(num, size)
        num += size
        # print(num)

        if arr[i] > i:
            check = False

        result[i] = num
        numbers.append(num)
        numbers.sort()

    if not check:
        print("IMPOSSIBLE")
    else:
        print(*result)
