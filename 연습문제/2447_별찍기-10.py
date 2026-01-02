import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def draw_stars(n):
    if n == 1:
        return ['*']
    
    Stars = draw_stars(n//3)
    
    L = []
    
    for s in Stars:
        L.append(s * 3)
    
    for s in Stars:
        L.append(s + ' '*(n//3) + s)
        
    for s in Stars:
        L.append(s * 3)

    return L

N = int(input())
print('\n'.join(draw_stars(N)))