import sys
input = sys.stdin.readline
from collections import deque

r,c,t = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(r)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

air_cleaner = []
for i in range(r):
    for j in range(c):
        if a[i][j] == -1:
            air_cleaner.append((i,j))
def solve():
    new_a = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if a[x][y] > 0 :
                dirty = a[x][y] // 5
                count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and a[nx][ny] != -1:
                        new_a[nx][ny] += dirty
                        count += 1
                a[x][y] -= (dirty * count)
                
    for x in range(r):
        for y in range(c):
            a[x][y] += new_a[x][y]
    
        
    # 공기 청정기 작동
    top = air_cleaner[0][0]
    
    for i in range(top - 1, 0, -1):
        a[i][0] = a[i-1][0]

    for i in range(c-1):
        a[0][i] = a[0][i+1]
    
    for i in range(top):
        a[i][c-1] = a[i+1][c-1]
    for i in range(c-1,1,-1):
        a[top][i] = a[top][i-1]
    a[top][1] = 0
    
    bottom = air_cleaner[1][0]
    
    for i in range(bottom+1,r-1):
        a[i][0] = a[i+1][0]
    
    for i in range(c-1):
        a[r-1][i] = a[r-1][i+1]
    
    for i in range(r-1,bottom,-1):
        a[i][c-1] = a[i-1][c-1]
     
    for i in range(c-1,1,-1):
        a[bottom][i] = a[bottom][i-1]
    a[bottom][1] = 0
    
for _ in range(t):
    solve()

result = 0
for i in range(r):
    for j in range(c):
        if a[i][j] != -1:
            result += a[i][j]
print(result)