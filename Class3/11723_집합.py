import sys
input = sys.stdin.readline

m = int(input())

s = set()
for _ in range(m):
    command = input().split()

    if len(command) == 1:
        if command[0] == "all":
            s = set([str(i) for i in range(1,21)])
        elif command[0] == "empty":
            s = set()
        continue


    op, x = command[0], command[1]

    if op == "add":
        s.add(x) 
    elif op == "remove":
        s.discard(x) 
    elif op == "check":
        print(1 if x in s else 0)
    elif op == "toggle":
        if x in s:
            s.discard(x)
        else:
            s.add(x)

        
