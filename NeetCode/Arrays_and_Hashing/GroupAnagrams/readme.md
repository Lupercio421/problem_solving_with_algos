# Group Anagrams - HashMap and Arrays

## Intuition

- At first, it made sense to use a `sort()` method on the `strs` array, that way, the `strs[i]` are ordered together by alphabetical order. But sorting will cause the time complexity to be `log(n)`.
- I then considered what if we find a way to use the a `HashMap`, so that the values of the keys will be the group of `strs[i]` that are anagrams of eachother

## Algorithm

- Use python's `defaultdict(list)
- FOr every string in `strs`, a `count` aray will hold all potential 0-26 values of the `strs[i]` word

## Implementation

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return list(res.values())
```
