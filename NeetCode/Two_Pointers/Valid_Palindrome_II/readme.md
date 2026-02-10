# Valid Palindrome II / Two Pointers

You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.

## Intuition

The question states that you can remove `at most` one character from the string to allow it to become a palindrome. The inital examples displayed characters at the ends of the string that would be best candidates to be removed. So begin by removing either the left most character or right most character.

## Approach

- Create a `l` pointer starting at `index = 0`, and a `r` pointer starting at `index = len(s) - 1` of the `s` string
- While `l` is less than `r`, do a boolean check to check if the characters are not the same, indicating a invalid palindrome
- `skipL` will be a substring of `s` from `l+1` up until but not including `r+1`. `skipR` will be a substring of `s` from `l` up until `r` (non-inclusive)
- Becuase we have reached the `at most` one character deletion, we perform a string equality on `skipL` and it's reverse. We check the same for `skipR`. If both fail, then the strings are not palindromes, and we return `false`
- The `l` pointer is increased, and the `r` pointer is decreased after the check on the `s[l] != s[r]` is `false`
- Return `true` if and when the `l` and `r` pointer meet, indicating a valid palindrome

## Complexity

- Time complexity: O(n)
- Space complexity: O(n)

## Code

### Python

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:

        l,r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL,skipR = s[l+1:r+1], s[l:r]
                return ((skipL == skipL[::-1]) or (skipR == skipR[::-1]))
            
            l,r = l+1, r-1
        
        return True
        
```

### Java

```java
class Solution {
    public boolean validPalindrome(String s) {
        int l = 0, r = s.length() - 1;

        while (l < r){
            if (s.charAt(l) != s.charAt(r)){
                return isPalindrome(s.substring(0,l) + s.substring(l+1)) || isPalindrome(s.substring(0,r) + s.substring(r+1));
            }
            l++;
            r--;
        }
        return true;
    }

    private boolean isPalindrome(String s){
        int l = 0, r = s.length() - 1;

        while (l < r){
            if (s.charAt(l) != s.charAt(r)){
                return false;
            }

            l++;
            r--;
        }
        return true;
    }
}
```

## Notes
