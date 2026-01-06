import sys
input = sys.stdin.readline
from collections import deque

n, goal = map(int,input().split())

def bfs(start):
    queue = deque()
    queue.append((start,0))
    visited = [-1] * 100001
    cnt = 0
    min_sec = sys.maxsize
    while queue:
        current, sec = queue.popleft()
        
        if goal == current:
            if sec <= min_sec:
                min_sec = sec
                cnt += 1
                continue
        
        if 0 <= current * 2 <= 100000:
            if visited[current*2] == -1 or visited[current*2] == sec + 1:
                visited[current*2] = sec + 1
                queue.append((current*2,sec+1))
            
        if 0 <= current + 1 <= 100000 :
            if visited[current+1] == -1 or visited[current+1] == sec + 1:
                visited[current+1] = sec + 1
                queue.append((current+1,sec+1))
        
        if 0 <= current - 1 <= 100000 :
            if visited[current-1] == -1 or visited[current-1] == sec + 1:
                visited[current-1] = sec + 1
                queue.append((current-1,sec+1))
            
    return min_sec,cnt

min_sec,cnt = bfs(n)
print(min_sec)
print(cnt)