import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)

sudoku = [list(map(int,input().rstrip())) for _ in range(9)]

empty = [] 
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
square = [[False] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append((i,j))
        else:
            row[i][sudoku[i][j]] = True
            col[j][sudoku[i][j]] = True
            square[(i//3)*3 + (j//3)][sudoku[i][j]] = True
            
def is_valid(x,y,num):
    if row[x][num] :
        return False
    elif col[y][num] :
        return False
    elif square[(x//3)*3+(y//3)][num] :
        return False
    return True
        
def dfs(idx):
    if idx == len(empty):
        for i in range(9):
            print(''.join(map(str,sudoku[i])))
        sys.exit(0)
        
    x, y = empty[idx]
    for num in range(1,10):
        if is_valid(x,y,num):
            sudoku[x][y] = num
            row[x][num] = True
            col[y][num] = True
            square[(x//3)*3+(y//3)][num] = True
            dfs(idx+1)
            sudoku[x][y] = 0
            row[x][num] = False
            col[y][num] = False
            square[(x//3)*3+(y//3)][num] = False
    
dfs(0)
    