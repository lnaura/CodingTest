import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]

nums.sort()

def get_mode(nums):
    counts = Counter(nums)

    max_freq = max(counts.values())

    modes = [num for num, freq in counts.items() if freq == max_freq]
    
    modes.sort()

    if len(modes) > 1:
        return modes[1]
    else:
        return modes[0]

avg = sum(nums) / n
if avg >= 0:
    print(int(avg + 0.5))
else:
    print(int(avg - 0.5))
print(nums[n//2])
print(get_mode(nums))
print(nums[-1] - nums[0])