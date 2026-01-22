import sys
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())

s1_len = len(s1)
s2_len = len(s2)
dp = [[''] * (s2_len+1) for _ in range(s1_len+1)]

for i in range(1, s1_len+1):
    for j in range(1,s2_len+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + s1[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                
print(len(dp[s1_len][s2_len]))
print(dp[s1_len][s2_len])

#-------------------------------------------------
# Backtracking 방법

import sys
input = sys.stdin.readline

def solve():
    s1 = list(input().rstrip())
    s2 = list(input().rstrip())

    s1_len = len(s1)
    s2_len = len(s2)
    dp = [[0] * (s2_len+1) for _ in range(s1_len+1)]

    for i in range(1, s1_len+1):
        for j in range(1,s2_len+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    length = dp[s1_len][s2_len]
    print(length)
    
    if length > 0:
        result = []
        i, j = s1_len, s2_len
        while i > 0 and j > 0 :
            if s1[i-1] == s2[j-1]:
                result.append(s1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] >= dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        print("".join(reversed(result)))
solve()