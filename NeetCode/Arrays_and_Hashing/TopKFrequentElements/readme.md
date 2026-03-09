# Top K Frequent Elements - Dictionary, Array, and Bucket Sort

## Intuition

- Dictionaries is a great data structure to use to measure/compare frequencies of arrays.
- My first attempt was done with creating a `dict`, inserting the `num` in `nums` as the key, and the value being the count of the value in the `nums` array.
- In this failed attempt, I tried to use the `Counter.most_common(int)` method to get the key and the count of the `dict` created. This was trouble as I had to work with `tuples` after this. This attempt did not progress further.
- This new attempt made use of `Bucket Sort` by creating a `freq` array, with `len` of `nums`. This `freq` array will first hold empty `arrays`.

## Algorithm

- We will still build the `count` (`dict`) where the key is the `num` in `nums` and the value is the count this particular `num` appears in the `nums` array.
- Python's `dict.items()` will be used to populate the `freq` array. `count.items` returns a `value` and a `count`. `freq[count]` will append the `value`. If `100` appears `1` time in `nums`, `freq[1] == 100`.
- Once that is populated, we will reverse iterate the `freq` array, isolating the `value` in `freq[i]`, and appending that `value` to the `res` array. Once the `len(res)` reaches its desired `k` number of elements, return `res`

## Implementation

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for val,c in count.items():
            freq[c].append(val)

        resList = []

        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                resList.append(val)
                if len(resList) == k:
                    return resList
```

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> count = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];

        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for (int n : nums){
            count.put(n, count.getOrDefault(n,0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry: count.entrySet()){
            freq[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int index = 0;
        for (int i = freq.length - 1; i > 0 && index < k; i--){
            for (int n:freq[i]){
                res[index++] = n;
                if (index == k){
                    return res;
                }
            }
        }
        return res;
    }
}
```
