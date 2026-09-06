# Two Sum II - Input Array Is Sorted : Two Pointers

Given a *1-indexed* array of integers `numbers` that is already ***sorted in non-decreasing order***, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers index1 and index2, ***each incremented by one***, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
## Intuition

This appears to be another two pointers solution. The goal is to return an array of two numbers. The numbers represent the index of of the `numbers` array, whose values at those indices sum to the `target` value. The catch is that the returned index should be `1-indexed`. Meaning their value should be returned plus one.

## Approach

1. Initialize and assign two pointers. `l` to be `0`. `r` to be the length of `numbers` - 1.
2. While `l` is less than `r`.
    - Initialize and assign `curSum` to be the sum of `numbers[l]` plus `numbers[r]`.
    - If `curSum` is greater than `target`, decrement `r`.
    - If `curSum` is less than `target`, increment `l`.
    - Else, we have the indices whose values of `numbers` sum up to `target`. Return a new array with those indices, added by `1`.
3. Edge case to consider, perhaps no number in `numbers` sum to the target. In that case, return a `[0]` array.

## Complexity

- Time complexity: O(n)
- Space complexity: O(1)

## Code

### Java
<details>

<summary>Java attempt 1</summary>

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;

        while (l < r) {
            int curSum = numbers[l] + numbers[r];

            if (curSum > target) {
                r--;
            } else if (curSum < target) {
                l++;
            } else {
                return new int[] {l + 1, r + 1};
            }
        }
        return new int[0];
    }
}
```
</details>

## Notes

[Any additional notes or alternative approaches]
