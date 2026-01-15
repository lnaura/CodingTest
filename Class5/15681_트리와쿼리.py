import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, root, q = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [1] * (n+1)
visited = [False] * (n+1) 

def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node] :
            dfs(next_node)
            dp[node] += dp[next_node]

dfs(root)

for _ in range(q):
    u = int(input())
    print(dp[u])