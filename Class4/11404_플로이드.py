import sys
input = sys.stdin.readline

INF = sys.maxsize
n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0
    
for _ in range(m):
    start,end,cost = map(int,input().split())    
    graph[start][end] = min(graph[start][end], cost)
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])
            
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] >= INF:
            print(0,end=" ")
        else:
            print(graph[i][j],end=" ")
    print()