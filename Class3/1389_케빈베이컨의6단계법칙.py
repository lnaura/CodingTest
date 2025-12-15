import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

def bfs(x):
    queue = deque()
    visited = [0] * (n+1)
    visited[x] = 1
    queue.append(x)

    while queue:
        f = queue.popleft()
        for fd in friends[f]:
            if not visited[fd]:
                visited[fd] = visited[f] + 1
                queue.append(fd)
    return sum(v - 1 for v in visited if v > 0 )

min_num = sys.maxsize
for i in range(1,n+1):
    num = bfs(i)
    if min_num > num:
        min_num = num
        min_i = i

print(min_i)