import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
S = input().rstrip()

ans = 0
count = 0
i = 0
while i < (m - 1) :
    if S[i:i+3] == "IOI":
        i += 2
        count += 1

        if count == n:
            ans += 1
            count -= 1
    else:
        i += 1
        count = 0

print(ans)