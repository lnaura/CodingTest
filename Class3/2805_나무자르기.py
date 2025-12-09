import sys
input = sys.stdin.readline

n, m = map(int,input().split())

trees = list(map(int,input().split()))

def binary_search(start,end,target):
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for tree in trees:
            if tree > mid:
                result += tree - mid

        if result >= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(0,max(trees),m))