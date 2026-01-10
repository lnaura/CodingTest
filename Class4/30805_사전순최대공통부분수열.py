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

#-------------------------------------------------------
# set 활용.
import sys
input = sys.stdin.readline

a_len = int(input())
a = list(map(int,input().split()))

b_len = int(input())
b = list(map(int,input().split()))

max_a_index = -1
max_b_index = -1
sub_a = []
sub_B = []
result = []
while True:
    sub_a = a[max_a_index+1 :]
    sub_b = b[max_b_index+1 :]
    
    common_set = set(sub_a) & set(sub_b)
    
    if not common_set:
        break
    
    max_val = max(common_set)
    result.append(max_val)
    
    max_a_index += 1 + sub_a.index(max_val)
    max_b_index += 1 + sub_b.index(max_val)
    
print(len(result))
print(*result)