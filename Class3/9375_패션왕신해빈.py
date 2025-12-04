import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    clothes = dict()

    for _ in range(n):
        a,b = input().split()

        if b in clothes:
            clothes[b] += 1
        else:
            clothes[b] = 1
    result = 1
    for count in clothes.values():
        result *= (count + 1)
    
    print(result - 1)
