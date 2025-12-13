import sys
input = sys.stdin.readline

n = int(input())
fruits = list(map(int,input().split()))

fruit_count = {}
left = 0
max_len = 0

for right in range(n):
    if fruits[right] in fruit_count:
        fruit_count[fruits[right]] += 1
    else:
        fruit_count[fruits[right]] = 1

    while len(fruit_count) > 2:
        fruit_count[fruits[left]] -= 1
        if fruit_count[fruits[left]] == 0:
            del fruit_count[fruits[left]]
        left += 1
    
    max_len = max(max_len , right - left + 1)

print(max_len)
