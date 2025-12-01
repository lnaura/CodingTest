from collections import deque
import sys
input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):

    docs, which = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue = deque()
    for doc in range(docs):
        queue.append((priorities[doc],doc))
    
    count = 0

    while True:
        current = queue.popleft()

        if any(current[0] < other[0] for other in queue):
            queue.append(current)
        else:
            count += 1
            if current[1] == which:
                print(count)
                break

