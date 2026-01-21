import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

command = list(map(int,input().split()))

def get_cost(start,end):
    if start == 0:
        return 2
    if start == end:
        return 1
    if abs(start - end) == 2:
        return 4
    return 3

dp = {(0,0) : 0}

for target in command[:-1]:
    new_dp = {}
    for (l,r), cost in dp.items():
        if target != r :
            new_pos = (target,r)
            new_cost = cost + get_cost(l,target)
            if new_pos not in new_dp or new_dp[new_pos] > new_cost:
                new_dp[new_pos] = new_cost
        
        if target != l:
            new_pos = (l,target)
            new_cost = cost + get_cost(r,target)
            if new_pos not in new_dp or new_dp[new_pos] > new_cost:
                new_dp[new_pos] = new_cost
        
    dp = new_dp

print(min(dp.values()) if dp else 0)
