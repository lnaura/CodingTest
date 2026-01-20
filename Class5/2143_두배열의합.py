import sys
input = sys.stdin.readline

t = int(input())

n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))

sum_a = dict()
sum_b = dict()
for i in range(n):
    sub_sum = 0
    for j in range(i,n):
        sub_sum += a[j]
        if sub_sum in sum_a:
            sum_a[sub_sum] += 1
        else : 
            sum_a[sub_sum] = 1

for i in range(m):
    sub_sum = 0
    for j in range(i,m):
        sub_sum += b[j]
        if sub_sum in sum_b:
            sum_b[sub_sum] += 1
        else : 
            sum_b[sub_sum] = 1

result = 0
for s_a in sum_a:
    target_b = t - s_a
    
    if target_b in sum_b:
        result += sum_a[s_a] * sum_b[target_b]

print(result)