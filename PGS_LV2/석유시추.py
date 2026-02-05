from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
    result = [0] * m
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        visited[x][y] = True
        col = set()
        col.add(y)
        size = 1
        
        while queue:
            cx, cy = queue.popleft()
            
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if land[nx][ny] == 1:
                        visited[nx][ny] = True
                        size += 1
                        col.add(ny)
                        queue.append((nx,ny))
        for c in col:
            result[c] += size
            
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i,j)
    
    answer = max(result)
            
    return answer