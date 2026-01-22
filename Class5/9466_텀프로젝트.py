import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    global result
    visited[node] = True
    trace.append(node)
    nxt = pick[node]
    
    if visited[nxt]:
        if nxt in trace_set:
            idx = trace.index(nxt)
            result += trace[idx:]
        return 
    else:
        trace_set.add(nxt)
        dfs(nxt)
        
        
t = int(input())
for _ in range(t):
    n = int(input())
    pick = [0] + list(map(int,input().split()))
    
    visited = [False] * (n+1)
    result = []
    
    for i in range(1,n+1):
        if not visited[i]:
            trace = []
            trace_set = set()
            
            trace_set.add(i)
            dfs(i)
    
    print(n - len(result))