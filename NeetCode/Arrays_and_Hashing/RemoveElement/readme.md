# Remove Element - Arrays and Two Pointers

You are given an integer array `nums` and an integer ``val``. Your tas`k` is to remove all occurrences of ``val`` from `nums` in-place.

After removing all occurrences of ``val``, return the number of remaining elements, say `k`, such that the first `k` elements of `nums` do not contain ``val``.

Note:

The order of the elements which are not equal to `val` does not matter.
It is not necessary to consider elements beyond the first `k` positions of the array.
To be accepted, the first `k` elements of nums must contain only elements not equal to `val`.
Return `k` as the final result.

## Intuition

When I read the `in-place` phrase, I knew that no extra memory were to be used. And the optimal solution will most likely be O(N)

For the optimal solution, it would be best to use two pointers. Where the `L` pointer is at the start of the array, and the `R` pointer is at the end of the array. If the value of nums at `L` is the `val`, swap it with the `R` value. Before increasing the `L` pointer, check if the newly swapped value is `val`.

## Approach - Two Pointers

- Step 1: Initialize `i = 0` as the current position and `n` as the effective length of the array.

- Step 2: While `i < n`
  - If `nums[i]` is the `val`, decrement the `n` value by 1.
  - Swap `nums[i]` with `nums[n]`
  - Else, increment `i` by 1
- Step 3: return n

## Complexity

- Time complexity: `O(n)`
- Space complexity: `O(1)`

## Code

### Python - Two Pointers

```python
class Solution:
    # Remove in place
    # best to create a O(n) solution
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n
```

### Python - Brute Force

```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue
            else:
                tmp.append(num)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)
```

### Java - Two Pointers

```java
public class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0, n = nums.length;
        while (i < n) {
            if (nums[i] == val) {
                nums[i] = nums[--n];
            } else {
                i++;
            }
        }
        return n;
    }
}
```

## Notes
