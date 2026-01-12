import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(shark_x,shark_y,shark_size):
    queue = deque()
    queue.append((shark_x,shark_y,0))    
    visited = [[False] * n for _ in range(n)]
    visited[shark_x][shark_y] = True
    candidates = []
    while queue:
        cx, cy, dist = queue.popleft()
        
        if candidates and candidates[0][0] < dist:
            break
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if 0 < graph[nx][ny] < shark_size:
                    visited[nx][ny] = True
                    candidates.append((dist+1,nx,ny))
                    queue.append((nx,ny,dist+1))
                if graph[nx][ny] == 0 or graph[nx][ny] == shark_size:
                    visited[nx][ny] = True
                    queue.append((nx,ny,dist+1))
    if candidates:
        candidates.sort()
        return candidates[0]
    else:
        return
# 상어위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j 
            graph[i][j] = 0      
shark_size = 2
eaten_count = 0
total_time = 0

while True:
    
    result = bfs(shark_x, shark_y,shark_size)
    
    if result is None:
        break
    
    dist, nx, ny = result
    total_time += dist
    eaten_count += 1
    
    if eaten_count == shark_size:
        shark_size += 1
        eaten_count = 0
    
    shark_x, shark_y = nx, ny
    graph[shark_x][shark_y] = 0
    
print(total_time)