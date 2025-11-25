from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque(range(1,N+1))

while len(queue) > 1:
    queue.popleft()

    card_to_move = queue.popleft()
    queue.append(card_to_move)

print(queue[0])