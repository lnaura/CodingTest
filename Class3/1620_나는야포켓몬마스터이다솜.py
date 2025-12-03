import sys 
input = sys.stdin.readline

n, m = map(int,input().split())

name_list = []
name_dict = {}

for i in range(n):
    name = input().strip()

    name_list.append(name)
    name_dict[name] = i + 1


for _ in range(m):
    quest = input().strip()

    if quest.isalpha():
        print(name_dict[quest])
    elif quest.isdigit():
        print(name_list[int(quest)-1])
