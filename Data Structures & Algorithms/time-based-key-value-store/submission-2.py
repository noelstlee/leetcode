class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        feelings = self.timeMap.get(key, [])
        res = ""
        
        l, r = 0, len(feelings) - 1
        while l <= r:
            m = (l + r) // 2
            if feelings[m][1] <= timestamp:
                res = feelings[m][0]
                l = m + 1
            else:
                r = m - 1
        return res



        
        
        
