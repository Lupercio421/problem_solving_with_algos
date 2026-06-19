# Subarray Sum Equals K / HashMap & PrefixSums

You are given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

```txt
Input: nums = [2,-1,1,2], k = 2

Output: 4
```

Explanation: `[2]`, `[2,-1,1]`, `[-1,1,2]`, `[2]` are the subarrays whose sum is equals to k.

## Intuition - Brute Force

For each starting index, extend the subbary element by element, maintaining a running sum. Whenever the sum equals `k`, we count it.

## Approach - Brute Force

1. Initialize `res = 0`.
2. For each starting index `i`:
    - Set `sum = 0`.
    - For each ending index `j` from `i` to `n - 1`:
        - Add `nums[j]` to `sum`.
        - If `sum == k`, increment `res`.
3. Return `res`.

## Complexity - Brute Force

- Time complexity: *O($n^2$)*
- Space complexity: *O(1)*

## Code - Brute Force

```java
class Solution {
    public int subarraySum(int[] nums, int k) {

        int res = 0;

        for (int i = 0; i < nums.length; i++){
            int sum = 0;
            for (int j = i; j < nums.length; j++){
                sum += nums[j];
                if (sum == k) res++;
            }
        }
        return res;
    }
}
```

## Intuition - HashMap

## Algorithm - HashMap

1. Initialize `res = 0`, `curSum = 0`, and a hash map `prefixSums` with `{0:1}` (representing the empty prefix)
2. For each starting number in the array:
    - Add it to `curSum`.
    - Compute `diff = curSum - k`:
    - Add prefixSums[diff] to `res` (counts subbarays ending here with sum `k`).
    - Increment `prefixSums[curSum]` by `1`.
3. Return `res`.

## Code - HashMap

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        int curSum = 0;
        Map<Integer, Integer> prefixSums = new HashMap<>();
        prefixSums.put(0, 1);
        for (int i = 0; i < nums.length; i++){
            curSum += nums[i];
            int diff = curSum - k;
            res += prefixSums.getOrDefault(diff, 0);
            prefixSums.put(curSum, prefixSums.getOrDefault(curSum, 0) + 1);
        }
        return res;
    }
}
```

## Complexity - HashMap

- Time complexity: *O(n)*
- Space complexity: *O(n)*

## Notes

[Any additional notes or alternative approaches]
