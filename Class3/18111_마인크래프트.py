import sys
input=sys.stdin.readline

n,m,b = map(int,input().split())

lands = []
for _ in range(n):
    lands.extend(map(int, input().split()))

height_counts = [0] * 257

for land in lands:
    height_counts[land] += 1

min_sec = sys.maxsize
ans_h = 0

for target in range(257):
    build_cost = 0
    remove_cost = 0

    for h in range(257):
        if height_counts[h] == 0:
            continue
        
        count = height_counts[h]

        if h > target:
            remove_cost += (h - target) * count
        else:
            build_cost += (target - h) * count
        
    if remove_cost + b >= build_cost:
        total_time = remove_cost * 2 + build_cost
        
        if total_time <= min_sec:
            min_sec = total_time
            ans_h = target

print(min_sec, ans_h)