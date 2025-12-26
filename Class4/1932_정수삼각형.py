import sys
input = sys.stdin.readline

n = int(input())

dp = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(i+1):
        up_left = dp[i-1][j-1] if j > 0 else 0

        up_right = dp[i-1][j] if j < i else 0
        
        dp[i][j] = dp[i][j] + max(up_left,up_right)
        
print(max(dp[n-1]))