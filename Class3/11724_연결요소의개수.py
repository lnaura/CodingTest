import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
cnt = 0
def dfs(graph,v, visited):
    visited[v] = True
    for j in graph[v]:
        if not visited[j]:
            dfs(graph,j,visited)

for i in range(1,n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        cnt += 1
print(cnt)

#---------------------------------------------------
# BFS
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
cnt = 0

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)