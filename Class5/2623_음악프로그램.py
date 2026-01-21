import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1) 
for _ in range(m):
    line = list(map(int,input().split()))
    num = line[0]
    order = line[1:]
    for i in range(num-1):
        graph[order[i]].append(order[i+1])
        in_degree[order[i+1]] += 1

queue = deque()

for i in range(1,n+1):
    if in_degree[i] == 0:
        queue.append(i)

result = []
while queue:
    curr = queue.popleft()
    result.append(curr)
    
    for next in graph[curr]:
        in_degree[next] -= 1
        
        if in_degree[next] == 0:
            queue.append(next)

if len(result) == n:
    print(*result, sep="\n")
else:
    print(0)