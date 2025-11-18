# 두 수 a, b를 입력받습니다.
a, b = map(int, input().split())

# 1. 최대공약수(GCD) 구하기 (유클리드 호제법)
# (a, b)를 (b, a%b)로 계속 갱신하다가 b가 0이 되면 a가 최대공약수

# 임시 변수를 사용 (a_temp, b_temp)
a_temp, b_temp = a, b 
while b_temp != 0:
    a_temp = a_temp % b_temp
    # (a, b)를 (b, a%b)로 바꾸기 위한 swap
    a_temp, b_temp = b_temp, a_temp 

gcd = a_temp  # b_temp가 0이 될 때의 a_temp 값이 최대공약수

# 2. 최소공배수(LCM) 구하기 (공식 이용)
# LCM = (A * B) // GCD
lcm = (a * b) // gcd

print(gcd)
print(lcm)
