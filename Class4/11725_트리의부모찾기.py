from collections import deque 
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
parents_node = [0] * (n+1)
def bfs(x):
    parents_node[x] = x
    queue.append(x)
    
    while queue:
        cx = queue.popleft()
        for nx in graph[cx]:
            if not parents_node[nx]:
                parents_node[nx] = cx
                queue.append(nx)

bfs(1)
for i in range(2,n+1):
    print(parents_node[i])
    
#-------------------------------------------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parents_node = [0] * (n+1)

def dfs(x):
    for nx in graph[x]:
        if not parents_node[nx]:
            parents_node[nx] = x
            dfs(nx)

parents_node[1] = 1
dfs(1)
for i in range(2,n+1):
    print(parents_node[i])