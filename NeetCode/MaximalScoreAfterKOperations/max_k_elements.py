import heapq
import math
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        max_heap = []

        for num in nums:
            heapq.heappush(max_heap, -num)

        while k > 0:
            k -= 1

            max_element = -heapq.heappop(max_heap)
            ans += max_element
            print(str(ans))

            heapq.heappush(max_heap, -math.ceil(max_element/3))
        print("This is the answer: " + str(ans))
        return ans
    
solution = Solution()
nums = [1,10,3,3,3]
k = 3
solution.maxKelements(nums=nums, k=k)