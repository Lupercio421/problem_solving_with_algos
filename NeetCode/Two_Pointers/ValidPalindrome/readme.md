# Valid Palindrome - Two Pointers

Given a string `s`, return `true` if it is a `palindrome`, otherwise return `false`.

A `palindrome` is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

```text
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
```
```text
Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
```
## Intuition

Check the palindrome string directly in place using two pointers. With one pointer `l`, at the start, the other pointer `r` at the end. We move both pointers inward, skipping any characters that are not letters or digits. Whenever both pointers point to valid characters, we compare them in lowercase form.

## Approach

1. Initialize two pointers:
    - `l` at the start of the string
    - `r` at the end of the string
2. While `l` is less than `r`:
    - Move `l` forward until it points to an alphanumeric character.
    - Move `r` backward until it points to an alphanumeric character.
    - Compare the lowercase characters at `l` and `r`:
        - If they don't match, return `false`.
    Move both pointers inward `l += 1`, `r -= 1`.
3. If the loop finishes without mismatches, return `true`.

## Complexity

- Time complexity: O(n)
- Space complexity: O(1)

## Code

<details>

<summary>Java</summary>

```java
public class Solution {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;

        while (l < r) {
            while (l < r && !alphaNum(s.charAt(l))) {
                l++;
            }
            while (r > l && !alphaNum(s.charAt(r))) {
                r--;
            }
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            l++; r--;
        }
        return true;
    }

    public boolean alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
}
```
</details>

<details>

<summary>Python</summary>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
```
</details>

## Notes

The `alphaNum` method is there to help skip the non alpha numeric characters from being compared in lowercase format.
