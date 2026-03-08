# Longest Consecutive Sequence

Given an array of integers `nums`, return *the length* of the longest consecutive sequence of elements that can be formed.

A *consecutive sequence* is a sequence of elements in which each element is exactly `1` greater than the previous element. The elements *do not* have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

```text
Input: nums = [2,20,4,10,3,4,5]
Output: 4

Explanation: The longest consecutive sequence is [2, 3, 4, 5]
```

## Intuition - Brute Force

I originally thought of this as a two pointer solution. Where I can order the array to have the sequence be the right most values of the array. Let that be the first pass. Then in the second pass, while in some sort of range, ensure that for each num, num + 1 is the next num in the array. The logic of this will fail once a repetitive value exists.

### Approach - Brute Force

1. Convert the input list to a set for `O(1)` lookups.
2. Initialzie `res` to store the maximum streak length
3. For each number `num` in the original list:
    - Start a new streak count at 0
    - Set `curr =  num`
    - While `curr` exists in the set:
        - Increase the streak count
        - Move to the next number (`curr += 1`)
    - Update `res` with the longest streak found so far.
4. Return `res` after checking all numbers.

### Complextiy

- Time: `O(N*N)`
- Space: `O(N)`
  
### Code

#### Python

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        res = 0

        for n in nums:
            streak = 0
            curr = n
            while curr in numSet:
                streak += 1
                curr += 1
            res = max(streak, res)
        return res
```

#### Java

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        int res = 0;
        Set<Integer> store = new HashSet<>();
        for (int num : nums)
        {
            store.add(num);
        }

        for (int num : nums) 
        {
            int streak = 0, curr = num;
            while (store.contains(curr))
            {
                streak++;
                curr++;
            }
            res = Math.max(res, streak);
        }
        return res;
    }
}
```

## Intuition - HashSet

To stop recounting the same sequences, we only want to start counting when we find the `beginning` of a consecutive sequence.

A number is the start of a sequence if `num - 1` is `not` in the set. This guarantees that each consecutive counted exactly once.

Once we identify such a starting number, we simply keep checking if `num + 1`, `num + 2`, ... exist in the set and extend the streak as far as possible.

This is clean becuase each number in `nums` contributes to the sequence only one time.

### Approach

1. Convert the list into a set numSet for `O(1)` lookups.
2. Initialize `longest` to track the length of the longest consecutive sequence.
3. For each number `num` in `numSet`:
    - Check if `num - 1` is `not` in the set:
        - If true, begin the start of the sequence at `num`
        - Initialize `length = 1`
        - To keep in bounds of `nums`, do a while `num + length` exist in the set, increase the `length`
    - Find the max of `longests` by comparing `length`
4. Return `longest` after scanning all numbers.

## Complexity

- Time complexity: O(N)
- Space complexity: O(N)

## Code - HashSet

### Python - HashSet

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
```

### Java - HashSet

```java
public class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        int longest = 0;

        for (int num : numSet) {
            if (!numSet.contains(num - 1)) {
                int length = 1;
                while (numSet.contains(num + length)) {
                    length++;
                }
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}
```
