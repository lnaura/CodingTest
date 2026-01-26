import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

stack = [a[0]]

for i in range(1,n):
    if stack[-1] < a[i]:
        stack.append(a[i])
    else:
        idx = bisect.bisect_left(stack,a[i])
        stack[idx] = a[i]

print(len(stack))