import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]    

def union(parent,x,y):
    root_x = find_parent(parent,x)
    root_y = find_parent(parent,y)
    
    if root_x < root_y:
        parent[y] = root_x
    else:
        parent[x] = root_y
        
g = int(input())
p = int(input())

parent = [i for i in range(g+1)]
cnt = 0
g_info = [int(input()) for _ in range(p)]

for i in range(p):
    p_gate = find_parent(parent,g_info[i])
    
    if p_gate != 0:
        union(parent,p_gate, p_gate - 1)
        cnt += 1
    else:
        break
print(cnt)