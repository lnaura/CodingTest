import sys
input = sys.stdin.readline

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b

# 진실을 아는 사람 그룹 만들기
know_info = list(map(int,input().split()))
know_people = []
if know_info[0] > 0:
    know_people = know_info[1:]

if len(know_people) > 1:
    for i in range(1, len(know_people)):
        union(know_people[0],know_people[i])
        
parties = []
for _ in range(m):
    party_info = list(map(int,input().split()))
    people_count = party_info[0]
    party_people = party_info[1:]
    
    parties.append(party_people)
    
    if people_count > 1:
        for i in range(1, people_count):
            union(party_people[0],party_people[i])

result = 0
for party in parties:
    if not know_people:
        result += 1
        continue
    if find(party[0]) != find(know_people[0]):
        result += 1
        
print(result)