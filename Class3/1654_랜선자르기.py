import sys
input = sys.stdin.readline

k, n = map(int,input().split())

lancable_lens = []
for _ in range(k):
    lancable_lens.append(int(input()))

def binary_search(target,start,end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for lancable_len in lancable_lens:
            cnt += lancable_len // mid

        if cnt >= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(n,1,max(lancable_lens)))