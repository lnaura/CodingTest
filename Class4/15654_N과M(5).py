import sys
input = sys.stdin.readline

n,m = map(int,input().split())

n_nums = list(map(int,input().split()))
n_nums.sort()
seq = []
visited = [False] * n

def dfs():
    if len(seq) == m:
        print(*seq)
        return
    for i in range(n):
        if not visited[i]:
            seq.append(n_nums[i])
            visited[i] = True
            dfs()
            seq.pop()
            visited[i] = False
    
dfs()