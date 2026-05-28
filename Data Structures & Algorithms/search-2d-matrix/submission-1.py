class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search after concatenating all the rows of 2D matrix
        con = [0] * len(matrix) * len(matrix[0])
        i = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                con[i] = matrix[row][col]
                i += 1

        res = self.binarySearch(con, target)
        
        return False if res == -1 else True 
    
    @staticmethod
    def binarySearch(arr: List[int], target: int) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if target > arr[mid]: # too small
                low = mid + 1
            elif target < arr[mid]: # too big
                high = mid - 1
            else:
                return mid
        return -1
