import sys
from collections import deque
input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())

    visited = [-1] * 101
    next_place = dict()

    for _ in range(n):
        x, y = map(int, input().split())
        next_place[x] = y

    for _ in range(m):
        x, y = map(int, input().split())
        next_place[x] = y

    def bfs():
        queue = deque([1])
        visited[1] = 0

        while queue:
            current = queue.popleft()

            for i in range(1, 7):
                next_step = current + i
                
                if next_step == 100:
                    print(visited[current]+1)
                    return

                if next_step in next_place:
                    next_step = next_place[next_step]

                if next_step <= 100 and visited[next_step] == -1:
                    visited[next_step] = visited[current] + 1
                    queue.append(next_step)
        print(visited[100])
    bfs()
solve()
