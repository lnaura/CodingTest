import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

dp_l = [1] * n
dp_r = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if a[i] > a[j]:
            dp_l[i] = max(dp_l[i],dp_l[j]+1)
            
for i in range(n-2,-1,-1):
    for j in range(n-1,i-1,-1):
        if a[i] > a[j]:
            dp_r[i] = max(dp_r[i],dp_r[j]+1)
            
result = 0
for i in range(n):
    left = dp_l[i]
    right = dp_r[i]
    if result < left + right:
        result = left + right
print(result-1)
        