import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = list((map(int,input().split())))
num.sort()

seq = []
visited = [False] * n

def dfs():
    if len(seq) == m:
        print(*seq)
        return
    prev = 0
    for i in range(n):
        if not visited[i] and prev != num[i] :
            seq.append(num[i])
            visited[i] = True
            prev = num[i]
            dfs()
            seq.pop()
            visited[i] = False

dfs()
        