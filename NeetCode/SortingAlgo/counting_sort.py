from typing import List

class Solution:
  def integer_sort(self, nums: List[int]) -> List[int]:
    left, mid, right = 0, 0, len(nums)-1

    while (mid < right):
      if(nums[mid] == 0):
        nums[mid],nums[left] = nums[left],nums[mid]
        left += 1
        mid += 1
      elif (nums[mid] == 1):
        mid += 1
      elif (nums[mid] == 2):
        nums[right],nums[mid] = nums[mid],nums[right]
        right -= 1
    return nums

solution = Solution()
arr = [1,2,0,1,0,2,2,1,0]
print(solution.integer_sort(nums=arr))