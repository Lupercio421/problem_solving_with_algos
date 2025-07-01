from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ansArr = []

        for i in range(2):
            for n in nums:
                ansArr.append(n)
        return ansArr


solution = Solution()
nums = [1, 2, 1]
print("This is the getConcatenation solution: ", solution.getConcatenation(nums=nums))