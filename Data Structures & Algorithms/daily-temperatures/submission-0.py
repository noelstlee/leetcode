class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        res = []
        count = 0
        append = False

        for i in range(len(temperatures)):
            append = False
            count = 0
            for j in range(i + 1, len(temperatures)):
                count += 1
                if temperatures[i] < temperatures[j]: # warm
                    res.append(count)
                    append = True
                    break
            if append == False:
                res.append(0)
        
        return res

            