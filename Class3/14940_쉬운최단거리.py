import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

dist = [[-1]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
queue = deque()

def bfs(x,y):
    dist[x][y] = 0
    queue.append((x,y))
 
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    dist[nx][ny] = dist[cx][cy] + 1
                    queue.append((nx,ny))
                    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and dist[i][j] == -1:
            bfs(i,j)
            found = True
            break
    if found:
        break
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dist[i][j] = 0

for d in dist:
    print(*d)