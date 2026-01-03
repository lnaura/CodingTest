import sys
sys.setrecursionlimit(10**6)

lines = sys.stdin.readlines()
nums = []
for line in lines:
    nums.append(int(line))
        
def solve(start,end):
    if start > end:
        return
    
    root = nums[start]
    
    mid = end + 1
    
    for i in range(start + 1, end + 1):
        if nums[i] > root:
            mid = i
            break
    
    solve(start + 1, mid - 1)
    solve(mid,end)
    print(root)
        
solve(0, len(nums)-1)