import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
            
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0,0))
    
    cheese = []
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx,ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    visited[nx][ny] += 1
                    if visited[nx][ny] == 2:
                        cheese.append((nx,ny))
                elif graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
    if cheese:
        for x,y in cheese:
            graph[x][y] = 0
        return 1
    else:
        return 0

time = 0
while True:
    melted = bfs()
    
    if melted > 0:
        time += 1
    else:
        print(time)
        break