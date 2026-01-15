import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int,input().split())
parent = [i for i in range(v+1)]

graph = []
result = 0

for _ in range(e):
    a, b, c = map(int,input().split())
    graph.append((c,a,b))
graph.sort()

for cost, a, b in graph:
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result += cost
    
print(result)

#--------------------------------------------
# prim 알고리즘
import heapq
import sys

input = sys.stdin.readline

def prim():
    v, e = map(int,input().split())
    
    adj = [[] for _ in range(v+1)]
    for _ in range(e):
        u,nxt_v,w = map(int,input().split())
        adj[u].append((w,nxt_v))
        adj[nxt_v].append((w,u))
        
    visited = [False] * (v+1)
    
    heap = [(0,1)]
    result = 0
    count = 0
    
    while heap:
        weight,curr = heapq.heappop(heap)
        
        if visited[curr]:
            continue
        
        visited[curr] = True
        result += weight
        count += 1
        
        if count == v:
            break
        
        for next_w, next_node in adj[curr]:
            if not visited[next_node]:
                heapq.heappush(heap,(next_w,next_node))
    
    print(result)
prim()