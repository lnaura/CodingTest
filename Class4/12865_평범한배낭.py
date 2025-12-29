import sys
input = sys.stdin.readline

n, k = map(int,input().split())

stuff = [[0,0]]
for _ in range(n):
    stuff.append(list(map(int,input().split())))

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    weight = stuff[i][0]
    value = stuff[i][1]
    
    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k])

#-------------------------------------------
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k + 1)

for _ in range(n):
    w,v = map(int,input().split())
    
    for j in range(k,w-1,-1):
        dp[j] = max(dp[j],dp[j-w]+ v)
        
print(dp[k])