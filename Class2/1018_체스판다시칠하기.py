import sys
input = sys.stdin.readline

n,m = map(int,input().split())

board = [list(input().strip()) for _ in range(n)]
INF = 10e9

result = INF
for i in range(0,n-7):
    for j in range(0,m-7):
        count = 0

        for a in range(i,i+8):
            for b in range(j,j+8):
                current_cell = board[a][b]

                if (a + b) % 2 == 0:
                    if current_cell != 'W':
                        count += 1
                else:
                    if current_cell != 'B':
                        count += 1
                
        result = min(result, count, 64 - count)

print(result)