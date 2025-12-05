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

            