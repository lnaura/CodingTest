import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    in_degree[b] += 1

heap = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(heap,i)

result = []
while heap:
    curr = heapq.heappop(heap)
    result.append(curr)
    
    for next in graph[curr]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            heapq.heappush(heap,next)
    
print(*result)