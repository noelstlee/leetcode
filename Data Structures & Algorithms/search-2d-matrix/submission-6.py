class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            L, R = 0, len(row) - 1
            while L <= R:
                M = (L + R) // 2
                if row[M] > target:
                    R = M - 1
                elif row[M] < target:
                    L = M + 1
                else:
                    return True
        return False

        