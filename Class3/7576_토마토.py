from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

m, n = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

while queue:
    cx, cy = queue.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[cx][cy] + 1
                queue.append((nx,ny))

max_days = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        max_days = max(max_days, graph[i][j])

print(max_days - 1)