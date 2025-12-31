import sys
from collections import deque
input = sys.stdin.readline

n, goal = map(int,input().split())

def bfs(x):
    queue = deque()    
    queue.append(x)
    dist = [-1] * 100001
    dist[x] = 0
    while queue:
        node = queue.popleft()

        if node == goal:
            return dist[node]
        if 0 <= node * 2 <= 100000 and dist[node * 2] == -1:
            queue.appendleft(node * 2)
            dist[node * 2] = dist[node]
        
        if 0 <= node -1 <= 100000 and dist[node -1 ] == -1:
            queue.append(node-1)
            dist[node-1] = dist[node] + 1
        
        if 0 <= node + 1 <= 100000 and dist[node+1] == -1:
            queue.append(node+1)
            dist[node+1] = dist[node] + 1

print(bfs(n))