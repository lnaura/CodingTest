
while 1:
    a,b,c = map(int,input().split(" "))
    
    if a ==0 and b == 0 and c ==0 :
        break
    
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        print("right")
    else:
        print("wrong")


#------------------------------------------#

while True:
    # 1. 세 숫자를 리스트로 받습니다.
    nums = list(map(int, input().split()))
    
    # 2. 종료 조건 확인 (0 0 0 이면 합계가 0)
    if sum(nums) == 0:
        break
        
    # 3. 오름차순으로 정렬합니다.
    #    nums[0] = 가장 짧은 변
    #    nums[1] = 중간 변
    #    nums[2] = 가장 긴 변 (빗변 후보)
    nums.sort() 
    
    # 4. 피타고라스의 정리 확인 (가장 긴 변이 빗변일 경우)
    if nums[0]**2 + nums[1]**2 == nums[2]**2:
        print("right")
    else:
        print("wrong")