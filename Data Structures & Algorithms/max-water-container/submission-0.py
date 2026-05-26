class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amount of water:
        # heights[a] heights[b] where a < b.
        # water: min(heights[a], heights[b]) * (b - a)
        L, R = 0, len(heights) - 1
        maxWater = 0

        while L < R:
            water = min(heights[L], heights[R]) * (R - L)
            maxWater = max(water, maxWater)
            if heights[L] >= heights[R]:
                R -= 1
            else:
                L += 1
        
        return maxWater