import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
result = 0

v1 = [False] * n
v2 = [False] * (2*n)
v3 = [False] * (2*n)

def dfs(row):
    global result    
    
    if row == n:
        result += 1
        return
    
    for col in range(n):
        if not v1[col] and not v2[row+col] and not v3[row-col+n-1]:
            v1[col] = True
            v2[row + col] = True
            v3[row - col + n - 1] = True
            
            dfs(row + 1)
            
            v1[col] = False
            v2[row + col] = False
            v3[row - col + n - 1] = False

dfs(0)
print(result)