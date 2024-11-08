from typing import List

class Solution:
    def getDuplicates(self, nums: List[int]) -> List[int]:

        solutionHashMap = {}
        solutionArray = []

        for idx, val in enumerate(nums):
            if val not in solutionHashMap:
                solutionHashMap[val] = idx
            else:
                solutionArray.append(val)
        return solutionArray
    
test_list = [1,2,6,3,5,2,3]
solution = Solution()
print("This is the getDuplicate method: " + str(solution.getDuplicates(test_list)))