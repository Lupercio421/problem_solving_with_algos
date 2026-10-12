# 3Sum - Sorting + Two Sum | HashMap

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must *not* contain duplicate triplets.

```text
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

```

## Intuition - Two Pointers

After sorting the array, we can fix one number and then search for the other two using the two-pointer technique.

Sorting helps in two ways:

1. It lets us skip duplicates easily.
2. It ensures that moving the left or right pointer will increase or decrease the sum in a predictable way.

## Approach - Two Pointers

1. Sort the array to handle duplicates and enable two-pointer logic.
2. Loop through the array using index `i`:
    - Let `a = nums[i]`.
    - If `a > 0`, **break** (all remaining `sorted` numbers are positive). The sum will be `greater` than 0.
    - Skip duplicate values for the first number.
3. Set two pointers:
    - `l = i + 1`
    - `r = len(nums) - 1`
4. While `l < r`:
    - Compute `threeSum = a + nums[l] + nums[r]`.
    - If `threeSum > 0`, move `r` left.
    - If `threeSum < 0`, move `l` right.
    - If `threeSum == 0`:
        - Add the triplet to the result.
        - Move both pointers inward.
        - Skip duplicates at the left pointer.
5. Return the list of all valid triplets.

## Complexity - Two Pointers

- Time complexity = $O(n^2)$
- Space complexity = O(1)

### Java - Two Pointers
<details>

<summary>Java Two Pointers</summary>

```java
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0)
                break; //why? - because this signifies that after going through the values of the sorted sum, all numbers at nums[i + 1] , nums[i + 2] will be positive and NOT ZERO. So there is no way to get a sum of zero.
            if (i > 0 && nums[i] == nums[i - 1])
                continue; //this if condition is triggered when i > 0, not when i = 0. Thus, we are not comparing nums[0] with nums[-1]

            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum > 0) {
                    r--;
                } else if (sum < 0) {
                    l++;
                } else {
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++; //what purpose does this serve? Does this help avoid duplicated nums[l] values? - ensuring that after finding a valid triplet, the l pointer doesn't restart at the same value it just used.
                    }
                }
            }
        }
        return res;
    }
}
```
</details>

## Intuition - HashMap


- Time complexity: O(?)
- Space complexity: O(?)

## Code - Two Pointers

<details>

<summary>Java attempt 1</summary>

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Map<Integer, Integer> freqMap = new HashMap<>();
        //Why must the `freqMap` contain a frequency count of the values of nums, and the values of `nums[i]` and the values of `nums[j]`?
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            freqMap.put(nums[i], freqMap.get(nums[i]) - 1);
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            for (int j = i + 1; j < nums.length; j++) {
                freqMap.put(nums[j], freqMap.get(nums[j]) - 1);
                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;
                int target = -(nums[i] + nums[j]);
                if (freqMap.getOrDefault(target, 0) > 0) {
                    res.add(Arrays.asList(nums[i], nums[j], target));
                }
            }
            for (int j = i + 1; j < nums.length; j++) {
                freqMap.put(nums[j], freqMap.get(nums[j]) + 1);
            }
        }
        return res;
    }
}
```
</details>

## Notes

[Any additional notes or alternative approaches]
