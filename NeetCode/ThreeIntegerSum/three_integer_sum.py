from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # this is the resulting list array
        res = []
        # order of the triplets does not matter
        nums.sort()
        for i, a in enumerate(nums):
            # check that this isn't the first value in input array
            # check that a is the same value as before
            if i > 0 and a == nums[i-1]:
                continue

            l,r = i+1, len(nums) - 1
            #l and r can't be equal
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
    
solution = Solution()
numsList = [-1,0,1,2,-1,-4]
solution.threeSum(nums=numsList)
# print("This is threeSum result: " + solution.threeSum(nums=numsList))