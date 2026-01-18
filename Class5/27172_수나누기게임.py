import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().split()))

is_present = [False] * 1000001        
for x in cards:
    is_present[x] = True

scores = [0] * 1000001
for i in cards:
    for j in range(i*2,1000001, i):
        if is_present[j]:
            scores[i] += 1
            scores[j] -= 1
            
result = []      
for i in cards:
    result.append(scores[i])
print(' '.join(map(str,result)))