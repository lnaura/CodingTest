import sys
input= sys.stdin.readline
INF = sys.maxsize

n, s = map(int,input().split())
num = list(map(int,input().split()))

start = 0
min_len = INF
curr_sum = 0

for end in range(n):
    curr_sum += num[end]
    
    while curr_sum >= s:
        min_len = min(min_len,end - start + 1)
        curr_sum -= num[start]
        start += 1

if min_len == INF:
    print(0)
else:
    print(min_len)