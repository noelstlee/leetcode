class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        diff = 0
        
        for i in range(len(temperatures)):
            diff = 0
            index = 0
            dayCount = 0
            while diff >= 0 and (i + index) < len(temperatures):
                diff = temperatures[i] - temperatures[i + index]
                index += 1
            if diff >= 0:
                res.append(0)
            else:
                res.append(index - 1)
        
        return res
                
