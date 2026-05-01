class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row first
        for row in board:
            rowCheck = set()
            for num in row:
                if num != ".":
                    if num in rowCheck:
                        return False
                    rowCheck.add(num)
            rowCheck.clear()
        
        # check cols
        for i in range(9):
            colCheck = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in colCheck:
                        return False
                    colCheck.add(board[j][i])
            colCheck.clear()
        
        # check square
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                squareCheck = set()
                for i in range(3):
                    for j in range(3):
                        val = board[r + i][c + j]
                        if val != ".":
                            if val in squareCheck:
                                return False
                            squareCheck.add(val)
                squareCheck.clear()

        
        return True