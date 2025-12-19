from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]
    m = len(graph[0])
    queue = deque()

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    n_cnt = 0

    def bfs(x,y):
        visited[x][y] = True
        queue.append((x,y))

        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                        if graph[nx][ny] == graph[cx][cy]:
                            visited[nx][ny] = True
                            queue.append((nx,ny))

    for x in range(n):
        for y in range(m):
            if not visited[x][y]:
                bfs(x,y)
                cnt += 1

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 'R':
                graph[x][y] = 'G'
    
    visited = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if not visited[x][y]:
                bfs(x,y)
                n_cnt += 1
    print(cnt, n_cnt)
solve()