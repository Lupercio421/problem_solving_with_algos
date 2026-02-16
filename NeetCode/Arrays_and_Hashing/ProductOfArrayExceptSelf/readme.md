# Product of Array Except Itself / Prefix & Postfix products

Given an integer array `nums`, return an array output where `output[i]` is the product of all the elements of nums except `nums[i]`.

## Intuition

[Explain your initial approach and thought process]

## Approach

[Detailed steps of your solution strategy]

- Step 1
- Step 2
- Step 3

## Complexity

- Time complexity: O(?)
- Space complexity: O(?)

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

[Any additional notes or alternative approaches]