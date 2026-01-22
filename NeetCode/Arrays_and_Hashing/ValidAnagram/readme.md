# Valid Anagram - Python 3 - hash map

`Anagram` - a string that contains the exact same characters as another string, but the order of the characters can be different.

## Intuition

My first thoughts were to place the individual letters of the strings into a hash map. Where values of the keys are the counts of letters in the strings. If the frequency of the distinct letters in each string match, then we have an anagram.

## Approach

- Begin by checking if the lengths of the strings are not equal to eachother
- Instantiate two dictionaries, `countS` and `countT`
- Iterate through all the keys in the string `s` and string `t`
- Make each individual key of the `countS` and `countT` the distinct letter in `s` and `t` respectively
- For every key in `countS`, compare the value of key with the value of same key in `countT`. Return `False` if the value are not equal. Return `True` if you have left the comparison.

## Complexity

- Time complexity: O(s + t). `s` being the length of string `s`, and `t` being the length of string `t`
- Memory: O(1), we will have at most 26 distinct characters.

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
```
