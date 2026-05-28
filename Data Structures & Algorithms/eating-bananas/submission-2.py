class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for k in range(1, max(piles) + 1):
        #     if self.canEatAll(k, piles, h):
        #         return k
        # return -1
        L, R = 1, max(piles)
        before = False
        while L <= R:
            mid = (L + R) // 2
            if self.canEatAll(mid, piles, h) == True: # k could be less
                R = mid - 1
                k = mid
                before = True
            elif self.canEatAll(mid, piles, h) == False: # k need to be higher
                L = mid + 1
            elif before == True and self.canEatAll(mid, piles, h) == False:
                break
        return k

    
    @staticmethod
    def canEatAll(k: int, piles: List[int], h: int) -> bool:
        # time spent eating a pile
        time = 0
        for pile in piles:
            time += -(pile // -k)
        if time <= h:
            return True
        return False
