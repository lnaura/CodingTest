import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
matrix = [] 
for _ in range(n):
    r, c = map(int,input().split())
    matrix.append((r,c))

dp = [[INF] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0
    
for dist in range(1,n):
    for i in range(n - dist):
        j = i + dist
        for k in range(i,j):
            dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
            
print(dp[0][n-1])