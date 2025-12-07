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

#-----------------------------------------
# 브루트포스 + 라그랑주 네 제곱수 정리
import sys
input = sys.stdin.readline

def solve(n):
    if int(n**0.5)**2 == n:
        return 1
    
    for i in range(1,int(n**0.5)+1):
        rem = n - i**2
        if int(rem**0.5)**2 == rem:
            return 2
    
    for i in range(1, int(n**0.5)+1):
        rem1 = n - i**2
        for j in range(1, int(rem1**0.5)+1):
            rem2 = rem1 - j**2
            if int(rem2**0.5)**2 == rem2:
                return 3
    
    return 4

n = int(input())
print(solve(n))