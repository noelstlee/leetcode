class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            maxNum = -100000
            for j in range(i + 1, len(arr)):
                maxNum = max(maxNum, arr[j])
            arr[i] = maxNum
        arr[len(arr) - 1] = -1
        return arr
