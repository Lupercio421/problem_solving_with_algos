# Two Integer Sum - Dictionary/HashMap

You are given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have ***exactly one solution***, and you may not use the *same* element twice.

You can return the answer in any order.

```text
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Intuition

We can rearrange this equation to `num[j] = target - num[i]`. We can label `num[j]` as `diff`. So our logic  can be revolved around finding what that `diff` is and what corresponnding `i` index is in the `nums` array. Making this our key and value.

## Approach

1. Create a hash map to store the value and index of each element in the array.
2. Iterate through the array using index `i` and compute the complement of the current element, which is `target - nums[i]`.
3. Check if the `diff` exists in the hash map.
4. If it does, return the indices of the current element and its compliment.
5. If no such pari is found, return empty array.


## Complexity

- Time complexity: `O(n)`
- Space complexity: `O(n)`

## Code

### Python

```python
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            print("This is i: " + str(i))
            print("This is n: " + str(n))
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
    
numsList = [3,4,5,6]
targetVar = 7
solution = Solution()
solution.twoSum(nums = numsList, target=targetVar)
```

### Java

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if (map.containsKey(diff)){
                return new int[]{map.get(diff), i};
            } else {
                map.put(nums[i], i);
            }
        } return new int[] {};
    }
}
```

## Notes