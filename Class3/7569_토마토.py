from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int,input().split())
graphs = []
for _ in range(h):
    graphs.append([list(map(int,input().split()))for _ in range(n)])

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

queue = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if graphs[z][y][x] == 1:
                queue.append((z,y,x))

while queue:
    cz,cy,cx = queue.popleft()

    for i in range(6):
        nx = cx + dx[i]
        ny = cy + dy[i]
        nz = cz + dz[i]
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if graphs[nz][ny][nx] == 0:
                graphs[nz][ny][nx] = graphs[cz][cy][cx] + 1
                queue.append((nz,ny,nx))

max_days = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if graphs[z][y][x] == 0:
                print(-1)
                exit()
            max_days = max(max_days,graphs[z][y][x])

print(max_days - 1)

#----------------------------------------------
# 더 나은 코드
import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int,input().split())
graph = []
queue = deque()
unripe_tomatoes = 0

for z in range(h):
    layer = []
    for y in range(n):
        row = list(map(int,input().split()))
        for x in range(m):
            if row[x] == 1:
                queue.append((x,y,z,0))
            elif row[x] == 0:
                unripe_tomatoes += 1
        layer.append(row)
    graph.append(layer)

if unripe_tomatoes == 0:
    print(0)
    exit()

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

last_day = 0
while queue:
    cx,cy,cz, days = queue.popleft()
    last_day = days

    for i in range(6):
        nx,ny,nz = cx+dx[i],cy+dy[i],cz+dz[i]

        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = 1
                unripe_tomatoes -= 1
                queue.append((nx,ny,nz,days+1))
            
print(last_day if unripe_tomatoes == 0 else -1)
