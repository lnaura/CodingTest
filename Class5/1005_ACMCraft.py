import sys
from collections import deque
input = sys.stdin.readline
    
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    time = [0] + list(map(int,input().split()))
    
    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1)
    for _ in range(k):
        x, y = map(int,input().split())
        graph[x].append(y)
        degree[y] += 1
        
    w = int(input())
    
    queue = deque()
    dp = [-1] * (n+1)
    for i in range(1,n+1):
        if degree[i] == 0:
            queue.append(i)
            dp[i] = time[i]
            
    while queue:
        node = queue.popleft()
        
        if node == w:
            break
        for next_node in graph[node]:
            degree[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[node] + time[next_node])
            if degree[next_node] == 0:
                queue.append(next_node)
    
    print(dp[w])