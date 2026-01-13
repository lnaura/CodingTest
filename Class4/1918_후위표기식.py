import sys
input = sys.stdin.readline

ex = list(input().rstrip())

priority = {
    '*':2, '/':2,
    '+':1, '-':1,
    '(':0
}
stack = []
result = []
for char in ex:
    if 'A' <= char <= 'Z':
        result.append(char)
    
    elif char in '*/+-':
        while stack and priority[stack[-1]] >= priority[char]:
            result.append(stack.pop())
    
        stack.append(char)

    elif char == '(':
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
while stack:
    result.append(stack.pop())
print(''.join(result))