# Merge Strings Alternately - Two Pointers

You are given two strings, `word1` and `word2`. Construct a new string by merging them in `alternating` order, starting with `word1` — take one character from `word1`, then one from `word2`, and repeat this process.

If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.

Return the final merged string.

```
Example 1:

Input: word1 = "abc", word2 = "xyz"

Output: "axbycz"
```

## Intuition - Two Pointers II

We can create a `n` and `m` variable, where each variable holds the lengths of `word1` and `word2` respectively. By setting pointers `i` and `j` at 0, while either of them are less than `n` or `m`, we can keep appending the character at `i` or `j` from `word1` and `word2`. Increasing `i` or `j` as needed.

## Approach - Two Pointers II

1. Initialize two pointers, `i` and `j` at `0`, and an empty result list.
2. While `i < n` or `j < m` (where `n` and `m` are the lengths of the strings):
    - If `i < n` append `word1[i]` and increment `i`.
    - If `j < m` append `word2[j]` and increment `j`.
3. Return the joined result string.

## Complexity - Two Pointers II

- Time complexity: O(n + m)
- Space complexity: O(n + m) for the output string.
    - Where `n` and `m` are the lengths of the strings `word1` and `word2`, respectively.

## Code

<details>

<summary>Java - Two Pointers II</summary>

```java
class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder res = new StringBuilder();
        int n = word1.length();
        int m = word2.length();

        int i = 0, j = 0;

        while (i < n || j < m) {
            if (i < n) {
                res.append(word1.charAt(i++));
            }
            if (j < m) {
                res.append(word2.charAt(j++));
            }
        }
        return res.toString();
    }
}
```
</details>


## Notes

[Any additional notes or alternative approaches]
