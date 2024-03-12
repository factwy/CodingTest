# 13549
import sys
input = lambda: sys.stdin.readline().strip()

# visited
# bfs

from collections import deque

n, k = map(int, input().split())
my_time = [10 ** 9] * 100001
    
def bfs(time = 0):
    global n, k, my_time
    
    queue = deque()
    queue.append((n, time))
    my_time[n] = time
    while queue:
        x, time = queue.popleft()
        
        if x == k:
            continue
        if 0 <= x*2 <= 100000 and my_time[x] < my_time[x*2]:
            my_time[x*2] = time
            queue.appendleft((x*2, time))
        
        if 0 <= x+1 <= 100000 and my_time[x]+1 < my_time[x+1]:
            my_time[x+1] = time + 1
            queue.append((x+1, time+1))
            
        if 0 <= x-1 <= 100000 and my_time[x]+1 < my_time[x-1]:
            my_time[x-1] = time + 1
            queue.append((x-1, time+1))
            
bfs()
print(my_time[k])