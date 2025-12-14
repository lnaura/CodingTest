from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

maps = [list(input().strip()) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False] * m for _ in range(n)]

cnt = 0

def bfs(y,x):
    global cnt
    queue = deque()
    visited[x][y] = True
    queue.append((x,y))
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and not maps[nx][ny] == 'X':
                if maps[nx][ny] == 'P':
                    cnt += 1
                visited[nx][ny] = True
                queue.append((nx,ny))

for j in range(m):
    for i in range(n):
        if maps[i][j] == "I":
            bfs(j,i)
            break

if cnt > 0:
    print(cnt)
else:
    print("TT")


