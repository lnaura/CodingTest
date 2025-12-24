import sys
from collections import deque
input = sys.stdin.readline

a,b = map(int,input().split())
queue = deque()


def bfs(start,target,cnt):
    queue.append((start,cnt))
    while queue:
        num,cnt = queue.popleft()
        if num == target:
            print(cnt)
            return

        multinum = num * 2
        if multinum <= target:
            queue.append((multinum,cnt+1))
        
        plusnum = num*10 + 1
        if plusnum <= target:
            queue.append((plusnum,cnt+1))
    
    print(-1)
    return
        
bfs(a,b,1)
#---------------------------------------
# Greedy 풀이
import sys
input = sys.stdin.readline

a, b = map(int,input().split())
count = 1

while True:
    if b == a:
        print(count)
        break
    if (b % 2 != 0 and b % 10 != 1) or (b < a):
        print(-1)
        break
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
        
    count += 1