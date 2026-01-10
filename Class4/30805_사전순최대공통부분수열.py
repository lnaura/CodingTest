import sys
input = sys.stdin.readline

a_len = int(input())
a = list(map(int,input().split()))

b_len = int(input())
b = list(map(int,input().split()))

# 최댓값 찾기
result = []
max_a_index = -1
max_b_index = -1
a_index = 0
b_index = 0
               
while True:
    if max_a_index == a_len - 1 or max_b_index == b_len - 1:
        break
    max_num = 0
    for i in range(max_a_index+1,a_len):
        for j in range(max_b_index+1,b_len):
            if a[i] == b[j]:
                if max_num < a[i]:
                    max_num = a[i]
                    a_index = i
                    b_index = j
    if max_num == 0:
        break
    
    max_a_index = a_index
    max_b_index = b_index
    result.append(max_num) 

print(len(result))
print(*result)