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

#---------------------------------------------------
# Counter 이용
import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))

sum_a = []
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += a[j]
        sum_a.append(current_sum)

sum_b = []
for i in range(m):
    current_sum = 0
    for j in range(i, m):
        current_sum += b[j]
        sum_b.append(current_sum)
        
count_a = Counter(sum_a)
count_b = Counter(sum_b)

result = 0
for s_a in count_a:
    target_b = t - s_a
    result += count_a[s_a] * count_b[target_b]