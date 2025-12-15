import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

def bfs(x):
    queue = deque()
    visited = [0] * (n+1)
    visited[x] = 1
    queue.append(x)

    while queue:
        f = queue.popleft()
        for fd in friends[f]:
            if not visited[fd]:
                visited[fd] = visited[f] + 1
                queue.append(fd)
    return sum(v - 1 for v in visited if v > 0 )

min_num = sys.maxsize
for i in range(1,n+1):
    num = bfs(i)
    if min_num > num:
        min_num = num
        min_i = i

print(min_i)

#------------------------------------------------
# 플로이드 워셜 알고리즘 풀이
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

min_num = INF
for i in range(1,n+1):
    num = sum(graph[i][1:]) 
    if min_num > num :
        min_num = num
        min_i = i
print(min_i)

