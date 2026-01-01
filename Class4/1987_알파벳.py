import sys
input = sys.stdin.readline

def solve():

    r,c = map(int,input().split())
    graph = [list(input().rstrip()) for _ in range(r)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q = set([(0,0,graph[0][0])])
    ans = 1
    
    while q:
        x, y, visited = q.pop()
        ans = max(ans,len(visited))
        
        if ans == 26:
            print(26)
            return
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] not in visited:
                    q.add((nx,ny,visited + graph[nx][ny]))
    print(ans)

solve()