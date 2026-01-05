import sys
input = sys.stdin.readline

s = list(input().rstrip())
dump = list(input().rstrip())

stack = []
dump_len = len(dump)
for i in s:
    stack.append(i)
        
    if stack[-dump_len:] == dump:
        del stack[-dump_len:]

if stack:
    print(''.join(stack))
else:
    print("FRULA")