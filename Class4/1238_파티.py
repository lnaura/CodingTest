import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))

def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,start))
    
    distance = [INF] * (n+1)
    distance[start] = 0
    while heap:
        dist, node = heapq.heappop(heap)
        
        if dist > distance[node]:
            continue
        
        for next_node,cost in graph[node]:
            next_cost = cost + dist
            
            if next_cost < distance[next_node]:
                heapq.heappush(heap,(next_cost,next_node))
                distance[next_node] = next_cost
    return distance
    
max_sec = 0
x_dist = dijkstra(x)
for i in range(1,n+1):
    dist = dijkstra(i)
    sec = dist[x] + x_dist[i]
    if max_sec < sec:
        max_sec = sec
print(max_sec)

#------------------------------------------
# 역방향 그래프
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)] # 역방향 그래프 추가

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    rev_graph[v].append((u, t)) # 역방향 간선 저장

def dijkstra(start, g):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if dist > distance[node]:
            continue
            
        for next_node, cost in g[node]:
            next_cost = cost + dist
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))
                
    return distance

to_home = dijkstra(x, graph)

to_party = dijkstra(x, rev_graph)

max_sec = 0
for i in range(1, n + 1):
    if to_home[i] != INF and to_party[i] != INF:
        max_sec = max(max_sec, to_home[i] + to_party[i])

print(max_sec)