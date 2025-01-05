from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums) - 1
        m = 0

        while l <= r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1

solution = Solution()
nums=[-1,0,2,4,6,8]
target=4
solution.search(nums=nums, target=target)