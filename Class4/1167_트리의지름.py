import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    graph_info = list(map(int,input().split()))
    g = graph_info[0]
    n = graph_info[1:-1]
    for i in range(0, len(n), 2):
        graph[g].append((n[i],n[i+1]))
    
max_dist = 0
max_node = 0

def dfs(node,dist):
    global max_dist
    global max_node
    
    if dist > max_dist:
        max_dist = dist
        max_node = node
    
    for next_node,d in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, dist + d)

visited = [False] * (v+1)
visited[1] = True
dfs(1,0)

target_node = max_node
visited = [False] * (v+1)
visited[target_node] = True
max_dist = 0
dfs(target_node,0)

print(max_dist)