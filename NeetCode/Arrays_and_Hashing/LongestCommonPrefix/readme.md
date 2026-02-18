# Longest Common Prefix - Arrays and Slicing

You are given an array of strings `strs`. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string `""`.

## Vertical Scaling - Intuition

Compare the characters of each string column by column. Check if all strings have the same character at position `0`, then position `1`, then `2`, .... When we find a mismatch at position `i` or reach the end of the string, we found where the common prefix ends.

## Vertical Scaling - Approach

Use `strs[0]` to be the single string that will be compared to all the other strings in `strs`.

- Step 1: Iterate through each character positions starting from index `0`.
- Step 2: At each position `i`, check the character in the first string.
- Step 3: Compare this character against position `i` in every other string.
- Step 4: If any string is too short or has a different character, return the prefix up to index `i-1`.
- Step 5: If we complete the loop without returning, the entire first string is the common prefix.

## Complexity

- Time complexity: O(n*m)
- Space complexity: O(1)

## Code

### Vertical Scaling - Python

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
```

### Vertical Scaling - Java

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        for (int i = 0; i < strs[0].length(); i++){
            for (String s : strs) {
                if (i == s.length() || s.charAt(i) != strs[0].charAt(i)){
                    return s.substring(0,i);
                }
            }
        }
        return strs[0];
    }
}
```

## Notes
