import sys 
input = sys.stdin.readline

n = int(input())

for i in range(1,n+1):
    spaces = ' ' * (2*n - 2*i)
    stars = '*' * i
    print(stars + spaces + stars)

for i in range(n-1,0,-1):
    spaces = ' ' * (2*n - 2*i)
    stars = '*' * i
    print(stars + spaces + stars)
    