from collections import deque
import sys
input = sys.stdin.readline

computers = int(input())
n = int(input())

networks = [[] for _ in range(computers + 1)]
for _ in range(n):
    a,b = map(int,input().split())
    networks[a].append(b)
    networks[b].append(a)

visited = [False] * (computers+1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        cnt += 1

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return cnt - 1

print(bfs(networks,1,visited))

#-----------------------------------------
# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

computers = int(input())
n = int(input())
networks = [[] for _ in range(computers + 1)]

for _ in range(n):
    a, b = map(int, input().split())
    networks[a].append(b)
    networks[b].append(a)

visited = [False] * (computers + 1)

def dfs(v):
    visited[v] = True

    for i in networks[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(sum(visited)-1)
