n = int(input())
num_list = list(map(int,input().split(" ")))

count = [0] * n

for i in range(n):
    for j in range(1,num_list[i]):
        if num_list[i] % j == 0:
            count[i] += 1

c = 0
for i in count:
    if i == 1:
        c += 1

print(c)

#-----------------------------------------------#
n = int(input())
num_list = list(map(int, input().split()))

prime_count = 0

for num in num_list:
    if num == 1:  # 1은 소수가 아님
        continue
    
    is_prime = True  # 일단 소수라고 가정
    
    # 2부터 (자신의 제곱근)까지 검사
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            is_prime = False  # 약수를 찾았으니 소수가 아님
            break             # 더 이상 검사할 필요 없음 (중요!)
            
    if is_prime:
        prime_count += 1

print(prime_count)