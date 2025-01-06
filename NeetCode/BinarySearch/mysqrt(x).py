class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 2, x // 2
        while l <= r:
            mid = (l + r) // 2
            num = mid * mid
            if num < x:
                l = mid + 1
            elif num > x:
                r = mid - 1
            else:
                return mid
        print("This is the result: " + str(mid))
        return r
    
solution = Solution()
x = 16
solution.mySqrt(x=x)