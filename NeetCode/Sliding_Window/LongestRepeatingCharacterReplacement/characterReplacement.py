class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0) #return default of 0
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1 #Take the count the char at the l index, and decrement by 1.
                l += 1
            res = max(res, r - l + 1)
        return res
    
solution = Solution()
s = "AAABABB"
solution.characterReplacement(s = s, k = 2) # 5