import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
num = list(map(int,input().split()))

def twopointer(num):
    left , right = 0, len(num) - 1
    min_sum = INF
    while left < right:
        curr_sum = num[left] + num[right]
        
        if abs(curr_sum) < min_sum:
            min_sum = abs(curr_sum)
            result = [num[left],num[right]]
            
        if curr_sum == 0:
            return result
        
        elif num[left] + num[right] < 0:
            left += 1
            
        elif num[left] + num[right] > 0:
            right -= 1
    return result

print(*twopointer(num))