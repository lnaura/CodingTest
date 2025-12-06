import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,cnt):
    q = deque()
    q.append((x,y))
    maps[y][x] = cnt
    houses_cnt = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] = cnt
                houses_cnt += 1
                q.append((nx,ny))
    return houses_cnt

n = int(input())
maps = [list(map(int,input().strip())) for _ in range(n)]

cnt = 1
houses = []
for j in range(n):
    for i in range(n):
        if maps[j][i] == 1:
            cnt += 1
            house = bfs(i,j,cnt)
            houses.append(house)
            

print(cnt - 1)
houses.sort()
for house in houses:
    print(house)