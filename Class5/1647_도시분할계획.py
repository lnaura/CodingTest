import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = []
for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append((c,a,b))

graph.sort()

parent = [i for i in range(n+1)]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
            
def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

total_cost = 0
edge_count = 0

for cost, a, b in graph:
    if find_parent(parent,a) != find_parent(parent,b):
        union(parent,a,b)
        total_cost += cost
        edge_count += 1
      
        if edge_count == n-2:
            break
    
print(total_cost if n > 2 else 0)