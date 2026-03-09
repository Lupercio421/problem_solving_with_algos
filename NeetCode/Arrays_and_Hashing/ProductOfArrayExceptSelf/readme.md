# Product of Array Except Itself / Prefix & Postfix products

Given an integer array `nums`, return an array output where `output[i]` is the product of all the elements of nums except `nums[i]`.

## Intuition

Without creating extra `prefix` and `suffix` arrays, we can reuse the result arrray and build the answer in two passes.

- In the `first pass`, fill the `res[i]` with the product of all elements to the left of `i` (this is the `prefix` product).
- In the `second pass`, multiply each `res[i]` with the product of all elements to the right of `i` (this is the `postfix` product).

By maintaining two running values - `prefix` and `postfix` - we avoid the need for separate `pref` and `suff` arrays.

## Approach/Algorithm

- Step 1: Initialize the result array `res` with all values set to 1. Or Initialize an empty array of length `nums.length`
- Step 2: Create a variable `prefix = 1`
- Step 3: First pass (left to right):
  - For each index `i`:
    - Set `res[i] = prefix` (the product of all elements to the left).
    - Update `prefix *= nums[i]`
- Step 4: Create a variable `postfix = 1`
- Step 5: Second pass (right to left):
  - For each index `i`:
    - Multiply `res[i]` by the `postfix` value
    - Update `postfix` by mutiplying itself with `nums[i]`. I.e: `postfix *= nums[i]`
- Step 6: return `res`

## Complexity

- Time complexity: O(N)
- Space complexity: O(1) extra space. O(N) space for the output array.

## Code

### Python

```python
class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:

        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
```

### Java

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];

        res[0] = 1;
        for (int i = 1; i < n; i++){
            res[i] = res[i-1] * nums[i-1];
        }

        int postfix = 1;
        for (int i = n - 1; i >=0; i--) {
            res[i] *= postfix;
            postfix *= nums[i];
        }
        return res;
    }
}  
```

## Notes
