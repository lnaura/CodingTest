import sys
input = sys.stdin.readline

n = int(input())
a = [[1, 1], [1, 0]]

def mul(a,b):
    result = [[0] * 2 for _ in range(2)]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000000007
    return result

def square(a,n):
    if n == 1:
        return a
    
    temp = square(a, n // 2)
    
    if n % 2 == 0:
        return mul(temp,temp)
    else:
        return mul(mul(temp,temp),a)

result  = square(a,n)
print(result[1][0])