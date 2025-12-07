# pypy3로 제출... 성공(python 시간초과)
import sys
input = sys.stdin.readline

n = int(input())
INF = 10e9

dp = [INF] * 50001

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3


for i in range(4,n+1):
    j = 1
    while (j * j) <= i:
        dp[i] = min(dp[i],dp[i - j * j] + 1)
        j += 1

print(dp[n])
    