from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # a...z

            for c in s:
                count[ord(c) - ord("a")] +=1

            res[tuple(count)].append(s) #group all anagrams w/ this particular count together. tuples are not mutable

        return list(res.values()) #O(m*n) m is the # of strings given, n is the length of each string

strs = ["act","pots","tops","cat","stop","hat"]
solution = Solution()
print("This is the group anagrams solution: ", solution.groupAnagrams(strs=strs))
    