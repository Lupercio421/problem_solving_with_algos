from typing import List

class Solution:
    def binarySolution(self, nums: List[int], element: int) -> bool:
        result = False

        binarySplitIndex = len(nums) // 2

        if (len(nums) == 0):
            return result
        elif (nums[binarySplitIndex] == element):
            result = True
            return result
        elif (element > nums[binarySplitIndex]):
            return self.binarySolution(nums[binarySplitIndex + 1:], element)
        else:
            return self.binarySolution(nums[:binarySplitIndex], element)

solution = Solution()
nums = [-3, -2, -1, 0, 1, 2, 3]
element = -2
print("answer: " + str(solution.binarySolution(nums=nums, element=element)))