# 4Sum - Two Sum | HashMap

You are given an integer array `nums` of size `n`, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- `a, b, c,` and `d` are **distinct**.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in **any order**.

```text
Note: [1,0,3,2] and [3,0,1,2] are considered as same quadruplets.
```

```text
Example 1:

Input: nums = [3,2,3,-3,1,0], target = 3

Output: [[-3,0,3,3],[-3,1,2,3]]
```

## Intuition

Two-pointer technique from 2Sum and 3Sum extend to this problem. After sorting, we fix the first two elements with nested loops, then use two pointers to find pairs that complete the target sum. The left pointer starts just after the second fixed element, and the right pointer starts at the end. 
We move them inward based on whether the current sum is too small or too large. Skipping duplicates at each level ensures unique quadruplets.

## Approach

1. Sort the array.
2. Iterate `i` from 0 to `n`, skipping duplicates.
3. For each `i`, iterate `j` from `i + 1` to `n`, skipping duplicates.
4. Use two pointers: `left = j + 1` and `right = n - 1`.
5. While `left < right`: 
    - If `sum` equals `target`, add quadruplet to the result array, and move both pointers while skipping duplicates.
    - If sum is less than target, increment `left`. 
    - If sum is greater than target, decrement `right`. 
6. Return the result list.

## Complexity

- Time complexity: $O(n^3)$
- Space complexity: 
    - $O(1)$ or $O(n)$ space depending on the sorting algorithm
    - $O(m)$ space for the output array.

## Code

### Java - Two Pointers

<details>

<summary>Java - two pointers</summary>

```java
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        // nums = [3,2,3,-3,1,0]
        // sortedNums = [-3,0,1,2,3,3]
        // Does it help to fix the first two numbers in nums? - Yes. this is what the boolean check on(nums[i] == nums[i-1]) and (nums[j] == nums[j - 1]) accomplishes
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            for (int j = i + 1; j < n; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;
                int left = j + 1, right = n - 1;
                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right]; //why is this a long? -- to avoid integer overflow
                    if (sum == target) {
                        res.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        left++;
                        right--;
                        while (left < right && nums[left] == nums[left - 1]) left++; //helps avoid reusing nums[left] and nums[left-1] if they are the same value
                        while (left < right && nums[right] == nums[right + 1]) right--; //helps avoid resuing nums[right] and nums[right + 1] if they are the same value
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        return res;
    }
}
```
</details>

### Python - Two Pointers

details>

<summary>Python - two pointers</summary>

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res
```
</details>


## Notes

[Any additional notes or alternative approaches]
