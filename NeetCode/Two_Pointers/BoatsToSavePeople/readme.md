# Boats to Save People - Two Pointers

You are given an integer array people where `people[i]` is the weight of the `ith` person, and an **infinite number of boats** where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.

Return the `minimum` number of boats to carry every given person.

```text
Example 1:
Input: people = [5,1,4,2], limit = 6

Output: 2
Explanation:
First boat [5,1].
Second boat [4,2]
```
## Intuition

Since each boat can carry at most two people and has a weight limit, we want to pair the heaviest person with the lightest person when possible. By sorting the weights, we can use two pointers: one at the heaviest person and one at the lightest. If they can share a boat, we move both pointers; otherwise, the heaviest person takes a boat alone.

## Approach

1. Sort the `people` array in ascending order.
2. Initiliaze two pointers, `left` at index `0`, right at the last index.
3. Initialize a boat counter to `0`.
4. While `left` is less than or equal to `right`:
    - Calculate the remaining weight after placing the heaviest person first (at `right`).
    - Decrement `right` and increment the boat count.
    - If the lightes person (at `left`) fits in the remaining capacity and `left` is still valid, increment `left`.
5. Return the boat count.

## Complexity

- Time complexity: O(n log n)
- Space complexity: O(1) or O(n) [depending on sorting algorithm]

## Code

<details>

<summary>Java - Sorting and Two Pointers</summary>

```java
class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int boatCount = 0;
        int l = 0;
        int r = people.length - 1;

        while (l <= r){
            int remainingWeight = limit - people[r];
            r -= 1;
            boatCount++;

            if (l <= r && remainingWeight >= people[l]){
                l++;
            }
        }
        return boatCount;
    }
}
```
</details>

<details>

<summary>Python - Sorting and Two Pointers</summary>

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #greedy
        #sort - nlogn

        people.sort()

        res = 0
        l,r = 0, len(people) - 1

        while l <= r:
            remainingWeight = limit - people[r]
            r -= 1
            res += 1
            
            if l <= r and remainingWeight >= people[l]:
                l += 1
        
        return res
```
</details>


## Notes

[Any additional notes or alternative approaches]
