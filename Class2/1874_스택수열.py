import sys
input = sys.stdin.readline

n = int(input())

targets = [int(input()) for _ in range(n)]

current = 1
stack = []
answer = []

for target in targets:
    while current <= target:
        stack.append(current)
        answer.append("+")
        current += 1

    if stack and stack[-1] == target:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit()
for a in answer:
    print(a)