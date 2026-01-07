import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(temp_graph):
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        cx,cy = queue.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    queue.append((nx, ny))
    safe_cnt = 0
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0:
                safe_cnt += 1
    return safe_cnt
                
# 빈칸 좌표 찾기
empty = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i,j))
            
max_cnt = 0  

# 빈칸 중 3개 뽑아서 벽세우기
for combo in combinations(empty,3):
    temp_graph = copy.deepcopy(graph)

    for i, j in combo:
        temp_graph[i][j] = 1
    
    current_safe_cnt = bfs(temp_graph)
    
    max_cnt = max(max_cnt, current_safe_cnt)

print(max_cnt)
