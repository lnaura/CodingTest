import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    
    if graph[y][x] == 1:
        graph[y][x] = 0

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        graph[y][x] = 1
    
    cnt = 0

    for j in range(n):
        for i in range(m):
            if dfs(i,j) == True:
                cnt += 1
    
    print(cnt)

# --------------------------------------
# BFS 풀이
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    graph[y][x] = 0

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx,ny))

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        graph[y][x] = 1
    
    cnt = 0

    for j in range(n):
        for i in range(m):
            if graph[j][i] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)