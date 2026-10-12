# Majority Element - Arrays and HashMap

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times in the array. You may assume that the majority element always exists in the array.

## Example

Input: nums = [5,5,1,1,1,5,5]
Output: 5

## Intuition - Hash Map

Majority element resonates with distinctness, so my intuiton was to use a dictionary/hashmap. One the hashmap is populated, then compare if the count is greater than `len(nums) // 2`.

### Approach - Hash Map

- Step 1: Create a hash map, `ansMap` to store the element frequencies.
- Step 2: Initialize `n` to hold the value of `len(nums) // 2`.
- Step 3: Populate the `ansMap` to hold the `num` as the key, and it's `count` in the array as the value.
- Step 4: Use `ansMap.items()` to get the `num`, and `count` as values.
  - Step 4.1: If `count` is greater than `n`, return `num`.

### Complexity - Hash Map

- Time complexity: O(N)
- Space complexity: O(N)

### Code - HashMap

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ansMap = {}
        n = len(nums) // 2

        for num in nums:
            ansMap[num] = 1 + ansMap.get(num, 0)

        for num, count in ansMap.items():
            if count > n:
                return num
        
```

```java
class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> ansMap = new HashMap<>();
        int n = nums.length; //division towards zero

        for (int num : nums){
            ansMap.put(num, ansMap.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : ansMap.entrySet()){
            if (entry.getValue() > n / 2){
                return entry.getKey();
            }
        }
        return -1;
    }
}
```

## Intuition - Boyer-More Voting Algorithm

The Boyer-Moore algorithm works by maintaining a candidate and a count. When we see the candidate, we increment the count; otherwise we decrement it. When the count reaches `0`, we pick a new candidte. Since the majority element appears more than half the time, it will survive this elimination process and remain as the final candidate.

## Approach - Boyer-More Voting Algorithm

- Step 1: Initialize `res` as the candidate and `count = 0`.
- Step 2: For each element `num`:
  - If `count == 0`, set `res = num`.
  - If `num == res`, increment `count`; otherwise decrement `count`.
- Step 3: Return `res` as the majority element.

### Code - Boyer-More Voting Algorithm

```python
class Solution:
    def majorityElement(self, nums):
        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res
```

```java
public class Solution {
    public int majorityElement(int[] nums) {
        int res = 0, count = 0;

        for (int num : nums) {
            if (count == 0) {
                res = num;
            }
            count += (num == res) ? 1 : -1;
        }
        return res;
    }
}
```

### Complexity - Boyer-More Voting Algorithm

- Time complexity: O(N)
- Space complexity: O(1)

## Notes
