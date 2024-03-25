import sys


def binary_search(x, y, z, k):
    start, end = 1, 2**31-1
    limit_food = [x, y, z]
    while start <= end:
        mid = (start + end) // 2

        total_index = 1
        food_type_index = -1
        food_index_index = -1

        for i in range(3):
            food_s, food_e = 0, limit_food[i]-1
            food_mid = (food_s + food_e) // 2
            while food_s <= food_e:
                food_mid = (food_s + food_e) // 2
                # food_mid : mid 앞 원소 개수

                if food[i][food_mid] == mid:
                    food_type_index = i+1
                    food_index_index = food_mid+1
                    break
                elif food[i][food_mid] < mid:
                    food_s = food_mid + 1
                else:
                    food_e = food_mid - 1

            total_index += food_mid
            if mid > food[i][food_mid]:
                total_index += 1

        if total_index == k:
            if food_type_index != -1 and food_index_index != -1:
                return food_type_index, food_index_index
            else:
                start = mid + 1
        elif total_index < k:
            start = mid + 1
        else:
            end = mid - 1


n = int(sys.stdin.readline())
food = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

q = int(sys.stdin.readline())
for _ in range(q):
    x, y, z, k = map(int, sys.stdin.readline().split())
    food_type, food_index = binary_search(x, y, z, k)
    sys.stdout.write(str(food_type) + " " + str(food_index) + "\n")
