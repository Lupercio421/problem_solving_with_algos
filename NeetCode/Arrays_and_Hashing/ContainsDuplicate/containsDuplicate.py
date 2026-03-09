from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        resultSet = set()
        for num in nums:
            if num not in resultSet:
                resultSet.add(num)
            else:
                return True
        return False

solution = Solution()
nums = [1,2,3,1]
print("This is the contains duplicate solution: ", solution.containsDuplicate(nums=nums))