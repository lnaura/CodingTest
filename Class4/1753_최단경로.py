import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

v,e = map(int,input().split())

start_node = int(input().rstrip())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))

def dijkstra(start_node,v,graph):
    dist = [INF] * (v+1)
    q = []
    heapq.heappush(q, (0, start_node))
    dist[start_node] = 0
    
    while q:
        d,now = heapq.heappop(q)
        
        if d > dist[now]:
            continue
        
        for i in graph[now]:
            next_node = i[0]
            cost = i[1]
            
            new_cost = d + cost
            
            if new_cost < dist[next_node]:
                heapq.heappush(q, (new_cost,next_node))
                dist[next_node] = new_cost
    return dist

dist = dijkstra(start_node,v,graph) 

for i in range(1,v+1):
    if dist[i] >= INF:
        print("INF")
    else:
        print(dist[i])
    