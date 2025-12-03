import sys
input = sys.stdin.readline

n,m = map(int, input().split())

heard_dict = {}
heard_see_list= []

for i in range(n):
    heard_dict[input().strip()] = i+1

for j in range(m):

    see_name = input().strip()

    if see_name in heard_dict:
        heard_see_list.append(see_name)

heard_see_list.sort()
num = len(heard_see_list)
print(num)
for i in range(num):   
    print(heard_see_list[i])

# ---------------------------------
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

heard = set(input().strip() for _ in range(n))

seen = set(input().strip() for _ in range(m))

result = sorted(list(heard & seen))

print(len(result))
for name in result:
    print(name)