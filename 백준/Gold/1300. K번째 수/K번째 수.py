import sys


def binary_search(n, k):
    start, end = 1, n*n
    while start <= end:
        mid = (start + end) // 2
        total_index = 0
        is_mid_in_arr = False
        check = set()
        cnt = 0

        for i in range(1, n+1):
            arr_s, arr_e = 1, n
            arr_mid = (arr_s + arr_e) // 2
            while arr_s <= arr_e:
                if i*arr_mid == mid:
                    is_mid_in_arr = True
                    break
                elif i*arr_mid > mid:
                    arr_e = arr_mid - 1
                else:
                    arr_s = arr_mid + 1

                arr_mid = (arr_s + arr_e) // 2

            total_index += (arr_mid-1)
            if mid > i*arr_mid:
                total_index += 1
            if mid == i*arr_mid:
                if not (mid in check):
                    check.add(mid)
                    total_index += 1
                else:
                    cnt += 1

        if is_mid_in_arr:
            if k-cnt <= total_index <= k:
                return mid
        if total_index >= k:
            end = mid - 1
        else:
            start = mid + 1


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

sys.stdout.write(str(binary_search(n, k)))
