import sys
import heapq
input = sys.stdin.readline

n, k = map(int,input().split())

jewels = [tuple(map(int,input().split())) for _ in range(n)]
jewels.sort()

bags = [int(input()) for _ in range(k)]
bags.sort()

heap = []
result = 0
idx = 0
for bag in bags:
    while idx < n and jewels[idx][0] <= bag:
        heapq.heappush(heap,-jewels[idx][1])
        idx += 1

    if heap:
        result += -heapq.heappop(heap)

print(result)