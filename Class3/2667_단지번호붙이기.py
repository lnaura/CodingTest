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

#--------------------------------------
# DFS 풀이
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    maps[y][x] = 0
    
    count = 1 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
       
        if 0 <= nx < n and 0 <= ny < n and maps[ny][nx] == 1:
            count += dfs(nx, ny)
            
    return count

n = int(input())
maps = [list(map(int, input().strip())) for _ in range(n)]

houses = []

for j in range(n):
    for i in range(n):
        if maps[j][i] == 1:
            house_count = dfs(i, j)
            houses.append(house_count)

houses.sort()

print(len(houses))
for h in houses:
    print(h)