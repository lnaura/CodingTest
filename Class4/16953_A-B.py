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
        