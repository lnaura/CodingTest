# 해결방법 1
n = int(input())

i = 666
cnt = 0
while True:
    if "666" in str(i):
        cnt += 1

    if cnt == n:
        print(i)
        break
    
    i += 1
