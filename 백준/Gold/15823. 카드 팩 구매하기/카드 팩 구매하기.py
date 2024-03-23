import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

start, end = 0, n
res = 0
while start <= end:
    mid = (start + end) // 2

    card_pack = set()
    l, r = 0, 0
    cnt = 0
    while l <= r < n and l < n:
        if card[r] in card_pack:
            while card[l] != card[r]:
                if card[l] in card_pack:
                    card_pack.remove(card[l])
                l += 1
            l += 1

        card_pack.add(card[r])

        if (r - l + 1) == mid:
            cnt += 1
            card_pack = set()
            r += 1
            l = r
        if r < n-1:
            r += 1

    if cnt >= m:
        res = max(res, mid)
        start = mid + 1
    else:
        end = mid - 1

sys.stdout.write(str(res))
