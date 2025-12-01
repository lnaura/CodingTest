import sys
input = sys.stdin.readline

n = int(input())

tiers = [int(input()) for _ in range(n)]
tiers.sort()
exception = int(n * 0.15 + 0.5)

if n == 0:
    print(0)
else:
    print(int(sum(tiers[exception:n-exception]) / (n - (2 * exception) ) + 0.5))