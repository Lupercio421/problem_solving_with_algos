from typing import List

class Solution:
    def merge_and_unmerge(self, nums: List[int], nums1: List[int]) -> List[int]:
        j,k = 0,0
        arr = []

        while j < len(nums) and k < len(nums1):
            if nums[j] <= nums1[k]:
                arr.append(nums[j])
                j += 1
            else:
                arr.append(nums1[k])
                k += 1

        while j < len(nums):
            arr.append(nums[j])
            j += 1

        while k < len(nums1):
            arr.append(nums1[k])
            k += 1

        nums[:len(nums)] = arr[:len(nums)]
        nums1[:len(nums1)] = arr[len(nums):]
        return arr

A = [4, 22, 100, 2223]
B = [33, 35]
# A = []
# B = []
solution = Solution()
solution.merge_and_unmerge(A,B) #O(n+m) run time, n & m are the lengths of the
print(A)
print(B)