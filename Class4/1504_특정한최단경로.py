import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
v1, v2 = map(int,input().split())

def dijkstra(start_node,n,graph):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0,start_node))
    distance[start_node] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            next_node = i[0]
            cost = i[1]
            
            new_cost = dist + cost
            
            if new_cost < distance[next_node]:
                heapq.heappush(q,(new_cost,next_node))
                distance[next_node] = new_cost
    return distance

result1, result2 = 0,0
dist = dijkstra(1,n,graph)
result1 += dist[v1]
result2 += dist[v2]

dist = dijkstra(v1,n,graph)
result1 += dist[v2]
result2 += dist[n]

dist = dijkstra(v2,n,graph)
result1 += dist[n]
result2 += dist[v1]

if min(result1,result2) >= INF:
    print(-1)
else:
    print(min(result1,result2))