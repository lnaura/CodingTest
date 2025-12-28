import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

a_len = len(a)
b_len = len(b)
dp = [[0]*(a_len + 1) for _ in range(b_len + 1)]
    
for i in range(1, b_len + 1):
    for j in range(1, a_len + 1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

result = 0
for s in dp:
    result = max(result,max(s))
print(result)