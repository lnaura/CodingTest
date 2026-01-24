import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    a,b,c,d = [], [], [], []
    for _ in range(n):
        r1,r2,r3,r4 = map(int,input().split())
        a.append(r1)
        b.append(r2)
        c.append(r3)
        d.append(r4)
    
    sum_ab = []
    sum_cd = []
    for i in range(n):
        for j in range(n):
            sum_ab.append(a[i] + b[j])
            sum_cd.append(c[i] + d[j])

    sum_ab.sort()
    sum_cd.sort()

    left = 0
    right = len(sum_cd) - 1
    result = 0
    len_tot = n * n

    while left < len_tot and right >= 0:
        curr_sum = sum_ab[left] + sum_cd[right]
    
        if curr_sum == 0:
            target_ab = sum_ab[left]
            target_cd = sum_cd[right]
            cnt1 = 0
            cnt2 = 0
        
            while left < len_tot and sum_ab[left] == target_ab:
                cnt1 += 1
                left += 1
            
            while right >= 0 and sum_cd[right] == target_cd:
                cnt2 += 1
                right -= 1
        
            result += (cnt1 * cnt2)
        
        elif curr_sum < 0:
            left += 1
        else:
            right -= 1
    
    print(result)
    
solve()