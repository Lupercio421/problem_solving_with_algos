# Find Target Indices After Sorting Array - Counting

You are given a **0-indexed** integer array `nums` and a target element `target`.

A **target index** is an index `i` such that `nums[i] == target`.

Return a list of the target indices of `nums` after sorting `nums` in **non-decreasing** order. If there are no target indices, return an empty list. The returned list must be sorted in **increasing** order.

```text
Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
```

## Intuition

Assing two count variables, `numsLessThanTarget` and `numsEqualToTarget`. `numsLessThanTarget` will keep track of the elements in `nums` that are strictly less than `target`.
`numsEqualToTarget` will provide the count of elements that are equal to target.

## Approach

1. Create two count variables
    - One to hold the number of elements less than the target
    - One to hold the number of elements equal to the target.
2. Initialize a empty `ArrayList`
3. Iterate from i = 0, through the length of the nums array.
4. Increment the respective count variables if they meet the boolean logic
5. Initialize a for loop for j, from 0 through the the number of elements equal to the target.
    - Add to the array list the number less than the target, offsetted by j.

## Complexity

- Time complexity: O(N)
- Space complexity: O(N)

## Code

### Java - Counting

```java
class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        //the target indices will be at most target, after being sorted
        //could this be done with two pointers?
        //count how many numbers are smaller than target
        int numsLessThanTarget = 0;
        int numsEqualToTarget = 0;
        List<Integer> ansArray = new ArrayList<>();
        for (int i = 0; i < nums.length; i++){
            if (nums[i] < target){
                numsLessThanTarget += 1;
            }
            if (nums[i] == target){
                numsEqualToTarget += 1;
            }
        }
        // FIX: Moved outside the counting loop — build ansArray once after counting is complete
        for (int j = 0; j < numsEqualToTarget; j++){
            ansArray.add(numsLessThanTarget + j); // FIX: offset j by numsLessThanTarget to get the actual sorted index
        }
        return ansArray;
    }
}
```

## Notes

[Any additional notes or alternative approaches]
