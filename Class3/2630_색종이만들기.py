import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int,input().split())) for _ in range(n)]

result = [0,0] # result[0] : 하얀색, result[1] : 파란색
def solution(x,y,N):
    color = paper[x][y]
    for j in range(y,y+N):
        for i in range(x,x+N):
            if color != paper[i][j] :
                solution(x, y, N//2)
                solution(x+N//2, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
        
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1
    
solution(0,0,n)            
print(result[0])
print(result[1])
