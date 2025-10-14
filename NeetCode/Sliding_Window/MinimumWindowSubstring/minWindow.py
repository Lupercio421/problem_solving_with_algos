class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT,window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            # does window[c] == count of T
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #update our result
                if (r - l + 1) < resLen: #size of current window minus result length
                    res = [l,r]
                    resLen = (r - l + 1)
                #pop from left of the window
                window[s[l]] -= 1
                print(window[s[l]])
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""

solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(solution.minWindow(s = s, t = t)) #BANC