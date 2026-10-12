# Sort Colors - Arrays

You are given an array `nums` consisting of `n` elements where each element is an integer representing a color:

- `0` represents red
- `1` represents white
- `2` represents blue

Your task is to `sort the array in-place` such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

You must not use any built-in sorting functions to solve this problem.

## Counting Sort

### Intuition

0, 1, and 2 are the only possible values. They are small enough to count how many times each appears in a single pass. We can overwrite the array in the second pass, placing the correct number of 0s, 1s, and 2s.

### Approach

1. Count the occurrences of `0`, `1`, and `2` in the array.
2. Overwrite the array:
    - Fill the first `count[0]` positions with `0`.
    - Fill the next `count[1]` positions with `1`.
    - Fill the remaining `count[2]` positions with `2`.

### Complexity

- Time complexity: O(n)
- Space complexity: O(1)

### Code

#### Python

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1

            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            
            i += 1
```

#### Java

```java
class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[3];
        for (int num : nums){
            count[num]++;
        }

        int index = 0;
        for (int i = 0; i < 3; i++){
            while (count[i]-- > 0){
                nums[index++] = i;
            }
        }
    }
}
```

## Three Pointers

### Intuition (Three Pointers)

The D.N.F algorithm partitions the array into three sections in a single pass. We maintain pointers for the boundary of 0s (left), the boundary of 2s (right), and the current element being examined. When we see a 0, we swap it to the left section. When we see a 2, we swap it to the right section. 1s naturally end in the middle.

### Approach (Three Pointers)

1. Initialize three pointers, `1` (boundary for `0`s), `i` (current element), and `r` (boundary for `2`s).
2. While `i <= r`:
    - If `nums[i]` is `0`, swap with `nums[l]`, increment both `l` and `i`.
    - If `nums[i]` is `2`, swap with `nums[r]`, decrement `r` (avoid incrementing `i`, because the swapped element must be checked).
    - If `nums[i]` is `1`, just increment `i`.

### Complexity (Three Pointers)

- Time complexity: O(n)
- Space complexity: O(1)

### Code (Three Pointers)

#### Python (Three Pointers)

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
```

#### Java (Three Pointers)

```java
public class Solution {
    public void sortColors(int[] nums) {
        int i = 0, l = 0, r = nums.length - 1;
        while (i <= r) {
            if (nums[i] == 0) {
                swap(nums, l, i);
                l++;
            } else if (nums[i] == 2) {
                swap(nums, i, r);
                r--;
                i--;
            }
            i++;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

## Notes

[Any additional notes or alternative approaches]
