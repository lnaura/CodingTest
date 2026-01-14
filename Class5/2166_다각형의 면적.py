import sys
input = sys.stdin.readline

n = int(input())
x_coords = []
y_coords = []
for _ in range(n):
    x,y = map(int,input().split())
    x_coords.append(x)
    y_coords.append(y)

x_coords.append(x_coords[0])
y_coords.append(y_coords[0])

sum_a = 0
sum_b = 0
for i in range(n):
    sum_a += x_coords[i] * y_coords[i+1]
    sum_b += x_coords[i+1] * y_coords[i] 

area = abs(sum_a - sum_b) / 2

print(f"{area:.1f}")