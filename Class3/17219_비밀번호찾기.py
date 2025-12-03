import sys
input = sys.stdin.readline

n,m = map(int,input().split())

site_dict = {}

for _ in range(n):
    site, password = input().split()
    site_dict[site] = password

for _ in range(m):
    print(site_dict[input().strip()])