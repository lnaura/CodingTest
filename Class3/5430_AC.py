from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    b = False
    is_reverse = False

    p = input().rstrip()
    n = int(input())
    num = input().strip()

    if n > 0:
        arr = deque(map(int,num[1:-1].split(',')))
    else:
        arr = deque()

    for i in p:
        if i == 'R':
            is_reverse = not is_reverse
        elif i == 'D':
            if arr:
                if is_reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                b = True
                break
    if not b:
        if is_reverse:
            arr.reverse()
        print(f"[{','.join(map(str,arr))}]")