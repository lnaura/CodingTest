import sys
input = sys.stdin.readline

n = int(input())

def get_primes(n):

    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j] = False
                
    return [i for i in range(n+1) if is_prime[i]]

prime = get_primes(n)

start = 0
end = 0
curr_sum = 0
cnt = 0

for end in range(len(prime)):
    curr_sum += prime[end]
    
    while curr_sum >= n:
        if curr_sum == n:
            cnt += 1
        curr_sum -= prime[start]
        start += 1

print(cnt)