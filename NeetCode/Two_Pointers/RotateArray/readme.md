# Rotate Array - Two Pointers

You are given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

```text
Example 1:

Input: nums = [1,2,3,4,5,6,7,8], k = 4

Output: [5,6,7,8,1,2,3,4]

Explanation:
rotate 1 steps to the right: [8,1,2,3,4,5,6,7]
rotate 2 steps to the right: [7,8,1,2,3,4,5,6]
rotate 3 steps to the right: [6,7,8,1,2,3,4,5]
rotate 4 steps to the right: [5,6,7,8,1,2,3,4]
```

## Intuition - Cyclical Traversal

We can rotate in-place by following cycles. Starting from any position, we move the element to its destination, then move the displaced element to its destination, and so on until we return to the starting position. If the cycle doesn't cover all elements (which happens when `n` and `k` share a common divisor), we start a new cycle from the next position. This ensures every element is moved exactly once.

## Approach - Cyclical Traversal

1. Compute `k = k % n` and initialize a counter for how many elements have been placed.
2. Start from index `0`. For each starting index:
    - Save the element at the current position.
    - Move to the next position `(current + k) % n`, swap the saved element with the element at this next position.
        - Repeat this step
    - Stop when we return to the starting index.
3.  If not all elements are placed, increment the starting index and repeat.
4. Continue until all `n` elements have been moved.

## Complexity - Cyclical Traversal

- Time complexity: O(n)
- Space complexity: O(1) extra space

## Code

<details>

<summary>Java - Cyclical Traversal</summary>

```java
import java.util.Arrays;

public class MainClass {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;

        Solution solution = new Solution();
        solution.rotate(nums, k);

        System.out.println(Arrays.toString(nums));
        // Expected: [5, 6, 7, 1, 2, 3, 4]
    }
}

class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;

        if (n == 0) {
            return;
        }

        k %= n;
        int count = 0;

        for (int start = 0; count < n; start++) {
            int current = start;
            int prev = nums[start];

            do {
                int nextIdx = (current + k) % n;
                int temp = nums[nextIdx];
                nums[nextIdx] = prev;
                prev = temp;
                current = nextIdx;
                count++;
            } while (start != current);
        }
    }
}
```
</details>

<details>

<summary>Python - Cyclical Traversal</summary>

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = start = 0

        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1
```
</details>
## Notes

[Any additional notes or alternative approaches]
