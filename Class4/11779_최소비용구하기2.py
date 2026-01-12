import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int,input().split())
    graph[a].append((b,cost))
    
start, end = map(int,input().split())

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [INF] * (n+1)
    distance[start] = 0
    prev_node = [0] * (n+1)
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if dist > distance[node]:
            continue
        
        for next_node, cost in graph[node]:
            next_cost = cost + dist
            
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                prev_node[next_node] = node
                heapq.heappush(heap,(next_cost,next_node))
    return distance, prev_node

dist, prev = dijkstra(start)
print(dist[end])

path = []
curr = end
while curr != 0:
    path.append(curr)
    if curr == start:
        break
    curr = prev[curr]

path.reverse()

print(len(path))
print(*path)