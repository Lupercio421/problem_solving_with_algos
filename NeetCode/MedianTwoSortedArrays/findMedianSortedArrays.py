from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 #will tell us the total elements in the left partition

        #ensure that A is the smaller array and swap if not
        if len(B) < len(A):
            A,B = B,A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 #A
            j = half - i - 2 #this is for B, arrays are indexed at 0, j starts at 0, i starts at 0

            #do we have a correct left partition
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            #this means our left partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                #odd number of elements
                if total % 2:
                    #median is the min of these two
                    return min(Aright, Bright)
                #even number of elements
                return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            #If we don't find the median, Aleft is too big
            elif Aleft > Bright:
                r = i - 1
            #Increase the size of the left partition from A
            else:
                l = i + 1

solution = Solution()
nums1 = [1,3]
nums2 = [2,4]
solution.findMedianSortedArrays(nums1=nums1, nums2=nums2)