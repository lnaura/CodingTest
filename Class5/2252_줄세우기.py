from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    in_degree[b] += 1

queue = deque()
for i in range(1,n+1):
    if not in_degree[i]:
        queue.append(i)

result = []
while queue:
    now = queue.popleft()
    result.append(now)
    
    for next in graph[now]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            queue.append(next)

print(*result)