import sys
input = sys.stdin.readline

n = int(input())

def draw_stars(n):
    if n == 3:
        return ['  *  ',' * * ','*****']
    
    stars = draw_stars(n//2)
    
    L = []
    
    for s in stars:
        L.append(' ' * (n//2) + s + ' ' *(n//2))
        
    for s in stars:
        L.append(s + ' ' + s)
    
    return L
        
print('\n'.join(draw_stars(n)))