import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):  
    start , end, cost = map(int,input().split())
    graph[start].append((end,cost))
    
s, e = map(int,input().split())

def dijkstra(start_node, n, graph):
    distance = [INF] * (n+1)
    
    q = []
    heapq.heappush(q,(0,start_node))
    distance[start_node] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            next_node = i[0]
            cost = i[1]
            
            new_cost = dist + cost
            
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q,(new_cost, next_node))
    return distance

result = dijkstra(s,n,graph)
print(result[e])