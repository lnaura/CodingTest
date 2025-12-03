import sys
input = sys.stdin.readline

t = int(input())

dp = [0] * 41
dp[0] = (1,0)
dp[1] = (0,1)

for i in range(2, 41):
    count0 = dp[i-1][0] + dp[i-2][0]
    count1 = dp[i-1][1] + dp[i-2][1]
    dp[i] = (count0, count1)

for _ in range(t):
    num = int(input())
    print(dp[num][0], dp[num][1])
