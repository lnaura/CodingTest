import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
t = int(input())

def bellman_ford(start,n,edges):
    dist = [INF] * (n+1)
    dist[start] = 0
    
    for i in range(n):
        for u, v, cost in edges:
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                
                if i == n-1:
                    return True
    return False
    
for _ in range(t):
    n,m,w = map(int,input().split())
    edges = []
    
    for _ in range(m):
        s,e,time = map(int,input().split())
        edges.append((s,e,time))
        edges.append((e,s,time))
    
    for _ in range(w):
        s,e,time = map(int,input().split())
        edges.append((s,e,-time))
    
    has_negative_cycle = bellman_ford(1,n,edges)
    if has_negative_cycle:
        print("YES")
    else:
        print("NO")