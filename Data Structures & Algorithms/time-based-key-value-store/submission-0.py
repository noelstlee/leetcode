class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))
        sorted(self.timeMap[key], key=lambda x:x[1])
        

    def get(self, key: str, timestamp: int) -> str:
        feelings = self.timeMap[key]

        for i in range(len(feelings) - 1, -1, -1):
            if feelings[i][1] <= timestamp:
                return feelings[i][0]
        
        return ""

        
        
        
