import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())

nums = sorted(list(set(map(int,input().split()))))

seq = []

def dfs(start):
    if len(seq) == m:
        print(*seq)
        return
    for i in range(start,len(nums)):
        seq.append(nums[i])
        dfs(i)
        seq.pop()
dfs(0)