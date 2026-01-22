# Contains Duplicate - Python 3 - set()

## Intuition

My first thoughts were to instantiate a dictionary. The dictionary will hold the number as the key, and it's count as the value. After going through the iteration, I realized that I would have to get the key and value from the dictionary. A set() was much better

## Approach

Instantiate a `set()`. Iterate through the nums list. If the number is not in the `set()`, add the number to the set. If the value is in the `set()`, immediately return `True`, we have encountered a duplicate value. If after all numbers have been compared to the `set()`, then we have no duplicates, return `False`.

## Complexity

- Time complexity: O(n), as we iterate at most through the length of nums.
- Space complexity: O(n), as we created a set() object with at most length of n.

## Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        resultSet = set()
        for num in nums:
            if num not in resultSet:
                resultSet.add(num)
            else:
                return True
        return False
```
