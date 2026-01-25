import sys
input = sys.stdin.readline

a, b = map(int,input().split())

def count_one(x):
    target = x + 1
    count = 0
    k = 0
    
    while (1<<k) <= x:
        cycle_len = 1 << (k + 1)
        
        count += (target // cycle_len) * (1 << k)
        
        remainder = target % cycle_len
        count += max(0, remainder - (1 << k))
    
        k += 1
    return count

result = count_one(b) - count_one(a-1)
print(result)