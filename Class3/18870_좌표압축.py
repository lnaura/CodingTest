import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

s_nums = sorted(list(set(nums)))

num_dict = {}
for idx,val in enumerate(s_nums):
    num_dict[val] = idx

print(*[num_dict[num] for num in nums])
