class Solution:
    # This is a method called solveNQueens within the class Solution. It takes two arguments, 
    # 'self' (referring to the instance of the class) and 'n' (an integer which denotes the size
    # of the chessboard and the number of queens). It is meant to return a list of list of strings.
    def solveNQueens(self, n: int):
        # Three sets are initialized here. col will hold the column indices where queens are already placed.
        # posDiag and negDiag hold the indices for the positive and negative diagonals respectively. This is 
        # done to keep track of the diagonals and columns which are already threatened by a queen.
        col = set()
        posDiag = set() #r+c
        negDiag = set() #r-c

        # res is an empty list that will hold all the valid board configurations. board is initialized 
        # to a NxN matrix filled with ".", indicating an empty board.
        res = []
        board = [["."]*n for i in range(n)]

        # This is the definition of a helper function backtrack that uses recursion to place the queens on the board.
        def backtrack(r):
            # If r equals n, it means we have placed n queens successfully and we have a valid board configuration.
            # We then add the configuration to our result list res and return from the function.
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
        # For each row, we try to place a queen in one of the n columns.
            for c in range(n):
                #Before placing a queen, we check if a queen already exists in the same column or diagonals. 
                # If it does, we skip this column and continue with the next one.
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # If it's safe to place a queen, we add the column index c to our col set and the diagonal indices
                # to the posDiag and negDiag sets. Then we place a queen ("Q") at the position on the board.
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                #We then move on to the next row and repeat the process using recursion.
                backtrack(r + 1)

                # Once we have explored all possible positions for a queen in the current row and the following 
                # rows (via recursion), we backtrack. We remove the queen from the board and the corresponding column 
                # and diagonal indices from the sets.
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        #We start the backtracking process from the first row (0th index).We start the backtracking process from the first row (0th index).
        backtrack(0)
        # Finally, we return the res list that contains all valid board configurations.
        return res

