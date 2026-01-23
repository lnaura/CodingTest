import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
cnt = 0

def dfs(x,y):
    global cnt
    
    visited[x][y] = 1
    
    if graph[x][y] == 'U':
        nx, ny = x - 1, y
    elif graph[x][y] == 'D':
        nx, ny = x + 1 , y
    elif graph[x][y] == 'R':
        nx, ny = x , y + 1
    elif graph[x][y] == 'L':
        nx, ny = x , y - 1
        
    if 0 <= nx < n and 0 <= ny < m :
        if visited[nx][ny] == 0:
            dfs(nx,ny)
        elif visited[nx][ny] == 1:
            cnt += 1
    visited[x][y] = 2

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            dfs(i,j)

print(cnt)
#-------------------------------------------
# union-find

import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    root_x = find_parent(parent,x)
    root_y = find_parent(parent,y)
    
    if root_x != root_y:
        parent[root_x] = root_y
        return True
    return False
         
n, m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]

parent = [i for i in range(n*m)]
total_sets = n * m

dirs = {
    'U': (-1,0), 'D': (1,0),
    'L': (0,-1), 'R' : (0,1)
}

for x in range(n):
    for y in range(m):
        dx, dy = dirs[graph[x][y]]
        nx, ny = x + dx, y + dy
        
        curr = x * m + y
        nxt = nx * m + ny
        
        if union(parent,curr,nxt):
            total_sets -= 1

print(total_sets)