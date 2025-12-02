import sys
input = sys.stdin.readline

m = int(input())
s = 0  

for _ in range(m):
    command = input().split()
    
    if command[0] == "all":
        s = (1 << 21) - 1
    elif command[0] == "empty":
        s = 0
    else:
        op = command[0]
        x = int(command[1])
        
        if op == "add":
            s |= (1 << x)
        elif op == "remove":
            s &= ~(1 << x)
        elif op == "check":
            if s & (1 << x):
                print(1)
            else:
                print(0)
        elif op == "toggle":
            s ^= (1 << x)