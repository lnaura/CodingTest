import sys
from collections import deque
input = sys.stdin.readline

n,l,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    group = []
    group.append((x,y))
    group_sum = graph[x][y]
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[nx][ny] - graph[cx][cy]) <= r:
                    queue.append((nx,ny))
                    group.append((nx,ny))
                    group_sum += graph[nx][ny]
                    visited[nx][ny] = True
    return group, group_sum

days = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group, group_sum = bfs(i,j)
                if len(group) >= 2:
                    group_avg = group_sum // len(group)
                    for x,y in group:
                        graph[x][y] = group_avg
                    flag = True
    if not flag:
        break
    else:
        days += 1
print(days)