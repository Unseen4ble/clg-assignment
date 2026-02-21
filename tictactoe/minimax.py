from checker import checker

class minimax:
    def __init__(self):
        self.check = checker()
    
    def moveLeft(self, grid, row):
        for i in range(row):
            for j in range(row):
                if(grid[i][j]==0):
                    return True
        return False
    
    def minimax(self, grid, dept, isMax, row, match_len, alpha, beta):
        score=self.check.winType(grid,match_len)

        if score == 10:
            return score

        if score == -10:
            return score
        
        if self.moveLeft(grid, row) == False:
            return 0
        
        if isMax:
            best = -10000

            for i in range(row):
                for j in range(row):
                    if grid[i][j] == 0:
                        grid[i][j] = -1
                        best=max(best, self.minimax(grid,dept+1,not isMax, row, match_len, alpha, beta))
                        grid[i][j] = 0
                        alpha = max(alpha,best)

                        if beta<=alpha:
                            break
                if beta<=alpha:
                    break

            return best
        
        else:
            best = 1000

            for i in range(row):
                for j in range(row):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                        best=min(best, self.minimax(grid,dept+1,not isMax, row, match_len, alpha, beta))
                        grid[i][j] = 0
                        beta=min(beta,best)
                        if beta<=alpha:
                            break
                if beta<=alpha:
                    break

            return best

    def bestmove(self, grid, row, match_len):
        bestVal = -1000
        bestMove = (-1,-1)

        for i in range(row):
            for j in range(row):
                if grid[i][j] == 0:
                    grid[i][j] = -1
                    moveVal = self.minimax(grid, 0, False, row, match_len, -1000, 1000)
                    grid[i][j] = 0

                    if moveVal > bestVal:
                        bestMove = (i,j)
                        bestVal = moveVal
        return bestMove
    

