import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0
max_num = max(map(max,board))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,depth,total):
    global ans
    if total + (4 - depth) * max_num <= ans:
        return
    if depth == 4:
        ans = max(ans,total)
        return
    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny,depth+1,total+board[nx][ny])
            visited[nx][ny] = False

def exceptions(x,y):
    global ans
    temp_sum = board[x][y]
    wings = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            wings.append(board[nx][ny])
    
    if len(wings) == 4 :
        wings.sort(reverse=True)
        wings.pop()
        ans = max(ans,temp_sum + sum(wings))
    elif len(wings) == 3 :
        ans = max(ans,temp_sum + sum(wings))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,board[i][j])
        visited[i][j] = False

        exceptions(i,j)
print(ans)