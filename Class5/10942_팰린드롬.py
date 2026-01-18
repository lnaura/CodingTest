import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
num = list(map(int,input().split()))

dp = [[False] * (n) for _ in range(n)]

for i in range(n):
    dp[i][i] = True
    
for i in range(n-1):
    if num[i] == num[i+1]:
        dp[i][i+1] = True


for len in range(3,n+1):
    for i in range(n - len + 1):
        j = i + len - 1
        if num[i] == num[j] and dp[i+1][j-1]:
            dp[i][j] = True
        
m = int(input())
for _ in range(m):
    s,e = map(int,input().split())
    if dp[s-1][e-1]:
        output("1\n")
    else:
        output("0\n")