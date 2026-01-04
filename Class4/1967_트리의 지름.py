import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
    

def get_distance(start_node):
    visited = [-1] * (n+1)
    visited[start_node] = 0
    
    def dfs(node, current_dist):
        for next_node,weight in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = current_dist + weight
                dfs(next_node, current_dist + weight)
    
    dfs(start_node,0)
    return visited

dist_from_1 = get_distance(1)

start_node = dist_from_1.index(max(dist_from_1))
        
final_dist = get_distance(start_node)
print(max(final_dist))