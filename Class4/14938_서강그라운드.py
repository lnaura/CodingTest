import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n , m , r = map(int,input().split())

items = [0] + list(map(int,input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for next_node,next_cost in graph[now]:
            cost = dist + next_cost
            
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost,next_node))
    
    return distance

result = 0
for i in range(1,n+1):
    dists = dijkstra(i)
    
    temp_sum = 0
    for j in range(1, n+1):
        if dists[j] <= m:
            temp_sum += items[j]
    result = max(result,temp_sum)
    
print(result)
