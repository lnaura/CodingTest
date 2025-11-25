import sys
input = sys.stdin.readline

n = int(input())

people = []

for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

rank = [1] * n

for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1

# 리스트의 요소를 공백으로 구분하여 출력하는 방법
print(*rank)
