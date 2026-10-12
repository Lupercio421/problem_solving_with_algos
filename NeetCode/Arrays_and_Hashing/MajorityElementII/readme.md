# Majority Element II - Arrays and HashMap

You are given an integer array `nums` of size `n`, find all elements that appear more than `⌊ n/3 ⌋` times. You can return the result in any order.

```txt
Example 1:

Input: nums = [5,2,3,2,2,2,2,5,5,5]

Output: [2,5]
```

## Intuition

Perhaps we initiate a default dictionary/hashmap.

## Approach

[Detailed steps of your solution strategy]

1. a
    - b
2. c
    - d
        - e

## Complexity

- Time complexity: O(?)
- Space complexity: O(?)

## Code

### Java

```java
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();

        for (int num : nums){
            count.put(num, count.getOrDefault(num, 0) + 1);

            if (count.size() > 2) {
                Map<Integer, Integer> newCount = new HashMap<>();
                for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
                    if (entry.getValue() > 1) {
                        newCount.put(entry.getKey(), entry.getValue() - 1);
                    }
                }
                count = newCount;
            }
        }

        List<Integer> res = new ArrayList<>();
        for (int key : count.keySet()) {
            int frequency = 0;
            for (int num : nums){
                if (num == key){
                    frequency++;
                }
            }
            if (frequency > nums.length / 3) {
                res.add(key);
            }
        }
        return res;
    }
}
```

### Python

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)
            for n,c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count

        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res
```

## Notes

[Any additional notes or alternative approaches]
