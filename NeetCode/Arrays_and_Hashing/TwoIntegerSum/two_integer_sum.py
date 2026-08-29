from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            print("This is i: " + str(i))
            print("This is n: " + str(n))
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
    
numsList = [3,4,5,6]
targetVar = 7
solution = Solution()
solution.twoSum(nums = numsList, target=targetVar)