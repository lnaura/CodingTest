import sys
input = sys.stdin.readline

n = int(input())

house = [list(map(int,input().split())) for _ in range(n)]

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

v = 1
for j in range(n):
    if house[0][j]:
        v = 0
    dp[0][j][0] = v
# 가로 0 세로 1 대각선 2
for i in range(1,n):
    for j in range(2, n):
        if not house[i][j]:
            dp[i][j][0] = dp[i][j-1][2] + dp[i][j-1][0]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            if house[i-1][j] == 0 and house[i][j-1] == 0:
                dp[i][j][2] = sum(dp[i-1][j-1])
                
print(sum(dp[n-1][n-1]))