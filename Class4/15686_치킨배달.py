import sys
from itertools import combinations
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int,input().split())
    
maps = [list(map(int,input().split())) for _ in range(n)]

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chickens.append((i,j))
        elif maps[i][j] == 1:
            houses.append((i,j))
            
min_city_chicken_dist = INF

for candidates in combinations(chickens, m):
    
    current_city_dist = 0
    
    for hx,hy in houses:
        min_dist_for_house = INF
        
        for cx,cy in candidates:
            dist = abs(hx-cx) + abs(hy-cy)
            
            if min_dist_for_house > dist:
                min_dist_for_house = dist
            
        current_city_dist += min_dist_for_house
        
        if current_city_dist > min_city_chicken_dist:
            break
    
    if current_city_dist < min_city_chicken_dist:
        min_city_chicken_dist = current_city_dist

print(min_city_chicken_dist)