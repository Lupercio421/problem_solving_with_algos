# Reverse String - Two Pointers

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array **in-place** with `O(1)` extra memory.

## Intuition

There is no strict comparison to be made for this problem. You can start a `l` and `r` pointer, at `0` and length of `string` - 1, respectively.
Let a place holder value store the character at pointer `l`, swap the character at pointer `r` for the character at `l`. Assign the character at pointer `r` to be the place holder. Then increment the `l` pointer, decrement the `r` pointer.

## Approach

1. Initialize two pointers, `l`, at index 0, and `r` at the last index.
2. While l < r:
    - Create a `placeHolder` / `temp` variable
    - Swap s[l] and s[r], while also making use of `temp`.
    - Increment `l` and decrement `r`.
3. The array `s` is now reversed in place.

## Complexity

- Time complexity: `O(n)`
- Space complexity: `O(1)`

## Code

### Java

```java
class Solution {
    public void reverseString(char[] s) {
        int L = 0;
        int R = s.length - 1;
        
        while (L < R){
            char placeHolder = s[L];
            s[L] = s[R];
            s[R] = placeHolder;
            L++;
            R--;
        }
    }
}
```

## Notes
