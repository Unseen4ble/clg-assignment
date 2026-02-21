class checker:
    def winType(self, grid, match_len):
        size = len(grid)

        for row in range(size):
            for col in range(size):

                # right
                if col + match_len <= size:
                    cur_player=grid[row][col]

                    if cur_player == 0:
                        continue

                    if all(grid[row][col + i] == cur_player for i in range(match_len)):
                        if grid[row][col]==1:
                            return -10
                        elif grid[row][col]==-1:
                            return 10

                # down
                if row + match_len <= size:
                    cur_player=grid[row][col]
                    if cur_player == 0:
                        continue
                    if all(grid[row + i][col] == cur_player for i in range(match_len)):
                        if grid[row][col]==1:
                            return -10
                        elif grid[row][col]==-1:
                            return 10

                # diagonal right-down
                if row + match_len <= size and col + match_len <= size:
                    cur_player=grid[row][col]
                    if cur_player == 0:
                        continue
                    if all(grid[row + i][col + i] == cur_player for i in range(match_len)):
                        if grid[row][col]==1:
                            return -10
                        elif grid[row][col]==-1:
                            return 10

                # diagonal left-down
                if row + match_len <= size and col - match_len + 1 >= 0:
                    cur_player=grid[row][col]
                    if cur_player == 0:
                        continue
                    if all(grid[row + i][col - i] == cur_player for i in range(match_len)):
                        if grid[row][col]==1:
                            return -10
                        elif grid[row][col]==-1:
                            return 10

        return 0
