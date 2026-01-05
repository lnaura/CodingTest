import sys
input = sys.stdin.readline

n,b = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(n)]

def mul(a,b):
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    
    return result

def square(a,b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a

    temp = square(a,b//2)
    
    if b % 2 == 0:
        return mul(temp,temp)
    else:
        return mul(mul(temp,temp),a)

result = square(A,b)

for row in result:
    print(*row)