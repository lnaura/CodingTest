import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
num = list(map(int,input().split()))
num.sort()

def twopointer():
    min_sum = INF
    for idx in range(n-2):
        left = idx + 1
        right = n - 1

        while left < right:
            curr_sum = num[left] + num[right] + num[idx]
        
            if min_sum > abs(curr_sum):
                min_sum = abs(curr_sum)
                result = [num[idx], num[left], num[right]]
            if curr_sum == 0:
                return result
            if curr_sum < 0:
                left += 1
            elif curr_sum > 0:
                right -= 1
    return result

result = twopointer()
print(*result)