class Solution:
    def maxArea(self, heights: List[int]) -> int:
    # find the min(heights[R],heights[L]) * (R - L)
        L, R = 0, len(heights) - 1
        res = 0

        while L < R:
            # compute area:
            area = min(heights[R], heights[L]) * (R - L)
            res = max(area, res) # save max area
            print(res)
            # since moving pointers, the (R - L) is always going to decline
            # so to make area max, we need to choose to move the smaller pointer and
            # hope it to be larger
            if heights[R] >= heights[L]:
                L += 1
            elif heights[R] < heights[L]:
                R -= 1
        return res