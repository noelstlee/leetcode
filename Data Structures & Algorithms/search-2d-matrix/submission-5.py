class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        topRow, botRow = 0, ROWS - 1

        # search for target's row first
        while topRow <= botRow: # common pitfall: remember botRow is the larger row
            row = (topRow + botRow) // 2
            if target > matrix[row][-1]: # too small
                topRow = row + 1
            elif target < matrix[row][0]: # too big
                botRow = row - 1
            else: # the target's row
                break
        
        if not (topRow <= botRow): # target doesn't exist in any of the rows
            return False
        
        L, R = 0, COLS - 1
        while L <= R:
            mid = (L + R) // 2
            if target > matrix[row][mid]: # too small
                L = mid + 1
            elif target < matrix[row][mid]: # too big
                R = mid - 1
            else:
                return True
        return False
        
