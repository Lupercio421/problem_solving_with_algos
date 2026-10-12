# Subarray Sums Divisible by K - Arrays and Prefix Sums

Given an integer array `nums` and an integer `k`, *return the number of non-empty ***subarrays*** that have a sum divisible by `k`*.

A **subarray** is a **contiguous** part of an array.

```text
Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

## Intuition

* Since they can be computed very easily, think in terms of running sums, where running_sum[i] = sum(nums[:i])
* Keep in mind that: running_sum[i] - running_sum[j] = sum(nums[i+1:j])
* We're looking for sum(nums[i+1:j]) % k = 0
* Thus, (running_sum[i] - running_sum[j]) % k = 0
* And consequently running_sum[i] % k = running_sum[j] % k


## Approach

Revist: https://neetcode.io/solutions/subarray-sums-divisible-by-k?utm_source=perplexity

## Complexity

- Time complexity: O(?)
- Space complexity: O(?)

## Code
<details>

<summary>Java attempt 1</summary>

```java
class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int[] map = new int[k];
        map[0] = 1;
        int count = 0, sum = 0;
        for (int num : nums){
            sum = (sum + num) % k;
            if (sum < 0){
                sum += k; //I.e, -1 % 5 = -1
            }
            //Why does the below two lines, inside a else statement, returns a bad answer?
            count += map[sum];
            map[sum]++;
        }
        return count;
    }
}
```
</details>

## Notes

[Any additional notes or alternative approaches]
