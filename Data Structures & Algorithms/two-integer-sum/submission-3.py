class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # need to find the indicies that sum up to target value
        # 1. try out every combination of summation nC2
        output = []
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index1 != index2:
                    if num1 + num2 == target:
                        output.append(index1)
                        output.append(index2)
                        return output
        return None
