class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numCount = defaultdict(int)
        length = 0

        for i in range(len(grid)):
            for k in range(len(grid[0])):
                numCount[grid[i][k]] += 1
                length += 1
            
        check = 1

        for key, val in numCount.items():
            if val >= 2:
                a = key
        
        for lenCheck in range(1, length + 1):
            if lenCheck not in numCount:
                b = lenCheck


        

        
        return [a, b]