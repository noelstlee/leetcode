class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
        arr = []
        for num in nums:
            if num != None:
                arr.append(num)
        for a in range(len(arr)):
            nums[a] = arr[a]
            
        return len(arr)