import sys
input = sys.stdin.readline

INF = 10000
N = int(input())

DP = [INF] * (N+1)
DP[0] = 0

for i in range(3,N+1):
    if DP[i - 3] != INF:
        DP[i] = DP[i-3] + 1

for i in range(5,N+1):
    if DP[i - 5] != INF:
        DP[i] = min(DP[i], DP[i-5] + 1)

if DP[N] >= INF:
    print(-1)
else:
    print(DP[N])
