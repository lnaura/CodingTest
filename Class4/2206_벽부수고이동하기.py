import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [list(map(int,input().rstrip())) for _  in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph):
    visited = [[[0,0] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    queue = deque()
    queue.append((0,0,0,1))
    
    while queue:
        cx, cy, w, cnt = queue.popleft()
        
        if cx == n-1 and cy == m-1:
            print(cnt)
            return 
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 0:
                    visited[nx][ny][1] = 1
                    queue.append((nx,ny,1,cnt + 1))
                elif graph[nx][ny] == 0 and not visited[nx][ny][w]:
                    visited[nx][ny][w] = 1
                    queue.append(((nx,ny,w,cnt + 1)))
                            
    print(-1)

bfs(graph)