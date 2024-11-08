from typing import List

class Solution:
    def segregate0and1(self, nums: List[int])-> List[int]:
        left,right = 0, len(nums)-1

        while left<right:
            while nums[left] == 0 and left < right:
                left += 1
            while nums[right] == 1 and left<right:
                right -= 1

            if left < right:
                nums[left] = 0
                nums[right] = 1
                left += 1
                right -= 1

        return nums
    
arr = [1,1, 0, 0, 1, 1,0]
solution = Solution()
print("Array after segregation") 
print(solution.segregate0and1(arr)) 
