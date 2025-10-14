from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0]*26, [0]*26 #can be implemented w/ arrays, l.c a through z
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 #ord, getting the asci values of this char. And substract from 'a'
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            print("ord(s2[r]): "+ str(ord(s2[r])))
            print("ord('a'): " + str(ord('a')))
            print(str(ord(s2[r]) - ord('a')))
            index = ord(s2[r]) - ord('a') #character that was just added to the window
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:#if the char is the same in arrays, increment matches
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: #by incr. this, we may have made it too large by 1, so we decrement it. That means they were equal, but with s2Count +1, matches is decrmented by 1
                matches -= 1
            
            # At index l, we remove the char from the window
            index = ord(s2[l]) - ord('a') #character that was just added to the window
            s2Count[index] -= 1 #character removed from the window
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1, s2)) #True