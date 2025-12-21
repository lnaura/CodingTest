from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

def bfs(start,target):
    visited = [False] * 10000
    queue = deque()
    
    queue.append((start,""))
    visited[start] = True
    
    while queue:
        current,cmd = queue.popleft()
        
        if current == target:
            return cmd
        # D 연산
        d_num = (current * 2) % 10000
        if not visited[d_num]:
            visited[d_num] = True
            queue.append((d_num,cmd+"D"))
        
        # S 연산
        s_num = 9999 if current == 0 else current - 1
        if not visited[s_num]:
            visited[s_num] = True
            queue.append((s_num,cmd+"S"))
        
        # L 연산
        l_num = (current % 1000) * 10 + (current // 1000)
        if not visited[l_num]:
            visited[l_num] = True
            queue.append((l_num,cmd+"L"))
        
        # R연산 
        r_num = (current % 10) * 1000 + (current // 10)
        if not visited[r_num]:
            visited[r_num] = True
            queue.append((r_num,cmd+"R"))
            
for _ in range(t):
    a, b = map(int,input().split())
    print(bfs(a,b))
