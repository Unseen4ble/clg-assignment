from minimax import minimax
from checker import checker

m= minimax()
c=checker()

row=int(input("enter the no of rows you want in your tic tac toe: "))
match_len=int(input("enter your match length: "))
if match_len>row:
    print("your match length cannot be greater than row")
size=row*row

#prints the tic tac toe grid work
def printer(grid,row):
    for i in range(row):
        for j in range(row):
            if grid[i][j]==0:
                print(" ",end="|")
            elif grid[i][j]==1:
                print("X",end="|")
            elif grid[i][j]==-1:
                print("O",end="|")

            # print(grid[i][j],end="|")
        print()
        for i in range(row):
            print("-",end="-")
        print()

#assigns x and o
def assigner(grid,row):
    
    # assigns x(1) min
    try:
        while True:
            pr1,pc1=map(int,input("player 1 turn: ").split())
            if grid[pr1-1][pc1-1] not in [1,-1]:
                if pr1-1<=row and pc1<=row:
                    grid[pr1-1][pc1-1]=1
                    cur_play=1
                else:
                    print("invalid choice")
                    return
                printer(grid,row)
                break
            else:
                print("shit already there")
    except ValueError:
        print("invalid input ")
        return
      
    a = c.winType(grid,match_len)
    if a == 10 or a == -10:
        print(f"{cur_play} won")
        return 5

    # checks if grid full
    if all(0 not in r for r in grid):
        print("Draw")
        return 5

    # player 2 bot move
    t = m.bestmove(grid, row, match_len)
    grid[t[0]][t[1]]=-1
    print("plyaer 2")
    cur_play=-1
    printer(grid, row)

    a = c.winType(grid,match_len)
    if a == 10 or a == -10:
        print(f"{cur_play} won")
        return 5

grid = [[0]*row for i in range(row)]
printer(grid,row)

# the game
while True:
    a = assigner(grid,row)
    if a==5:
        break

