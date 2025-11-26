import sys
input = sys.stdin.readline

k = int(input())
stack = []
for i in range(k):
    num = int(input())
    
    stack.append(num)

    if num == 0:
        stack.pop()
        stack.pop()
    
print(sum(stack))
        