class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L , R = 1, max(piles)
        before = False
        while L <= R:
            mid = (L + R) // 2
            if self.canEatAll(piles, mid, h) == True:
                R = mid - 1
                k = mid
                before = True
            elif self.canEatAll(piles, mid, h) == False:
                L = mid + 1
            elif before == True and self.canEatAll(piles, mid, h) == True:
                break
        return k

        
    

    def canEatAll(self, piles: List[int], k: int, h: int) -> int:
        time = 0
        for pile in piles:
            time += -(pile // -k)
        if time <= h:
            return True
        return False